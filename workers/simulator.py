import time
import random

from models.thermal import thermal
from models.workload import workload
from models.power import power
from models.system import system
from models.event_log import event_log
from models.psu import psu1


def simulator_loop():

    while True:

        #
        # =====================================
        # POWER OFF
        # =====================================
        #
        if system.power_state == "Off":

            workload.cpu_util = 0

            power.power_watts = 10

            if thermal.cpu_temp > thermal.inlet_temp:

                thermal.cpu_temp -= 0.3

            if not system.shutdown_logged:

                event_log.add(
                    "System Power Off",
                    "Warning"
                )

                system.shutdown_logged = True

            print(
                "POWER OFF",
                "TEMP=",
                round(thermal.cpu_temp, 1)
            )

            time.sleep(1)

            continue

        #
        # System back ON
        #
        system.shutdown_logged = False

        #
        # =====================================
        # CPU UTILIZATION RANDOM WALK
        # =====================================
        #
        workload.cpu_util += random.randint(-5, 5)

        if workload.cpu_util < 5:
            workload.cpu_util = 5

        if workload.cpu_util > 100:
            workload.cpu_util = 100

        #
        # =====================================
        # AUTO FAN CONTROL
        # =====================================
        #
        pwm = int(

            min(
                100,

                max(
                    30,

                    (thermal.cpu_temp - 30) * 2
                )
            )
        )

        thermal.fan1_pwm = pwm
        thermal.fan2_pwm = pwm

        #
        # =====================================
        # FAN RPM
        # =====================================
        #
        thermal.fan1_rpm = (

            int(thermal.fan1_pwm * 80)

            if thermal.fan1_enabled

            else 0
        )

        thermal.fan2_rpm = (

            int(thermal.fan2_pwm * 80)

            if thermal.fan2_enabled

            else 0
        )

        #
        # =====================================
        # HEAT MODEL
        # =====================================
        #
        heat = workload.cpu_util / 20

        cooling = (

            thermal.fan1_rpm +
            thermal.fan2_rpm

        ) / 3000

        thermal.cpu_temp += (

            heat -
            cooling

        ) * 0.15

        #
        # Ambient limit
        #
        if thermal.cpu_temp < thermal.inlet_temp:

            thermal.cpu_temp = thermal.inlet_temp

        #
        # =====================================
        # POWER MODEL
        # =====================================
        #
        power.power_watts = (

            80 +

            (workload.cpu_util * 1.8) +

            (thermal.fan1_rpm / 500) +

            (thermal.fan2_rpm / 500)

        )

        #
        # PSU update
        #
        psu1.update(
            power.power_watts
        )

        #
        # =====================================
        # HEALTH STATE
        # =====================================
        #
        if thermal.cpu_temp < 70:

            system.health = "OK"

        elif thermal.cpu_temp < 85:

            if system.health != "Warning":

                event_log.add(
                    "CPU temperature warning",
                    "Warning"
                )

            system.health = "Warning"

        elif thermal.cpu_temp < 100:

            if system.health != "Critical":

                event_log.add(
                    "CPU temperature critical",
                    "Critical"
                )

            system.health = "Critical"

        else:

            system.health = "Critical"

            event_log.add(
                "Thermal shutdown",
                "Critical"
            )

            system.power_state = "Off"

        #
        # =====================================
        # FAN1 FAILURE
        # =====================================
        #
        if (

            not thermal.fan1_enabled

            and

            not thermal.fan1_failure_logged

        ):

            event_log.add(
                "Fan1 failure detected",
                "Warning"
            )

            thermal.fan1_failure_logged = True

        #
        # =====================================
        # FAN2 FAILURE
        # =====================================
        #
        if (

            not thermal.fan2_enabled

            and

            not thermal.fan2_failure_logged

        ):

            event_log.add(
                "Fan2 failure detected",
                "Warning"
            )

            thermal.fan2_failure_logged = True

        #
        # =====================================
        # FAN1 RECOVERY
        # =====================================
        #
        if (

            thermal.fan1_enabled

            and

            thermal.fan1_failure_logged

        ):

            event_log.add(
                "Fan1 recovered",
                "OK"
            )

            thermal.fan1_failure_logged = False

        #
        # =====================================
        # FAN2 RECOVERY
        # =====================================
        #
        if (

            thermal.fan2_enabled

            and

            thermal.fan2_failure_logged

        ):

            event_log.add(
                "Fan2 recovered",
                "OK"
            )

            thermal.fan2_failure_logged = False

        #
        # =====================================
        # DEBUG
        # =====================================
        #
        print(

            "CPU=",
            workload.cpu_util,

            "TEMP=",
            round(
                thermal.cpu_temp,
                1
            ),

            "PWM=",
            thermal.fan1_pwm,

            "FAN1=",
            thermal.fan1_rpm,

            "FAN2=",
            thermal.fan2_rpm,

            "POWER=",
            round(
                power.power_watts,
                1
            )
        )

        time.sleep(1)