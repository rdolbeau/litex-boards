#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2021 Romain Dolbeau <romain@dolbeau.org>
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *
from litex.build.altera import AlteraPlatform
from litex.build.altera.programmer import USBBlaster

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # Clk / Rst
    ("adc_clk_10", 0, Pins("M9"), IOStandard("2.5-V LVTTL")),
    ("max10_clk1_50", 0, Pins("M8"), IOStandard("2.5-V LVTTL")),
    ("max10_clk2_50", 0, Pins("P11"), IOStandard("3.3-V LVTTL")),
    ("ddr3_clk_50", 0, Pins("N15"), IOStandard("1.5-V LVTTL")),
    # net_clk_25 (25 MHz) to Ethernet Transceiver
    # usb_clk_19 (19.2 Mhz) to USB OTG PHY
    # usb_clk_24 (24 MHz) to USB controller of UB2
    # ub2_clk_50 (50 mHz) to UB2 Max II CPLD

    # Leds
    ("user_led", 0, Pins("C7"), IOStandard("1.2-V LVTTL")),
    ("user_led", 1, Pins("C8"), IOStandard("1.2-V LVTTL")),
    ("user_led", 2, Pins("A6"), IOStandard("1.2-V LVTTL")),
    ("user_led", 3, Pins("B7"), IOStandard("1.2-V LVTTL")),
    ("user_led", 4, Pins("C4"), IOStandard("1.2-V LVTTL")),
    ("user_led", 5, Pins("A5"), IOStandard("1.2-V LVTTL")),
    ("user_led", 6, Pins("B4"), IOStandard("1.2-V LVTTL")),
    ("user_led", 7, Pins("C5"), IOStandard("1.2-V LVTTL")),

    # Buttons
    ("user_btn", 0, Pins("H21"), IOStandard("1.5-V LVTTL")),
    ("user_btn", 1, Pins("H22"), IOStandard("1.5-V LVTTL")),

    # Switches
    ("user_sw", 0, Pins("J21"), IOStandard("1.5-V LVTTL")),
    ("user_sw", 1, Pins("J22"), IOStandard("1.5-V LVTTL")),

    # CapSense I2C
    # AB2 & AB3 (SCL & SCA) # TODO 3.3-V

    # PowerMonitor I2C
    # Y3 & Y1 (SCL & SCA) & Y4 (Alert) # TODO 3.3-V
    
    # GPIOs
    ("gpio_0", 0, Pins(
        "W18 Y18 Y19 AA17 AA20 AA19 AB21 AB20",
        "AB19 Y16 V16 AB18 V15 W17 AB17 AA16",
        "AB16 W16 AB15 W15 Y14 AA15 AB14 AA14",
        "AB13 AA13 AB12 AA12 AB11 AA11 AB10 Y13",
        "Y11 W13 W12 WW11 V12 V11 V13 V14",
        "Y17 W14 U15 R13"
        ),
        IOStandard("3.3-V LVTTL")
    ),
    ("gpio_1", 0, Pins(
        "Y5 Y6 W6 W7 W8 V8 AB8 V7",
        "R11 AB7 AB6 AA7 AA6 Y7 V10 U7",
        "W9 W5 R9 W4 P9 V17 W3"
        ),
        IOStandard("3.3-V LVTTL")
    ),

    # SYS_RESET_n
    # AA2 # TODO 3.3-V

    # PWR_BUT
    # U6 # TODO 3.3-V

    # ADC1
    # F5, F4, J8, J9, J4, H3, K5 # TODO 2.5-V

    # Audio Codec
    # P14, R14, R15, P15, P18, P19, P20, P21, N21, N22, M21, M22 # TODO 1.5-V

    # Serial
    #("serial", 0,
    #    Subsignal("tx", Pins(""), IOStandard("")),
    #    Subsignal("rx", Pins(""), IOStandard(""))
    #),

    # DDR3 SDRAM
    # With a MT41K256M16HA-125:E 
    ("ddram", 0,
        Subsignal("a", Pins("E21 V20 V21 C20 Y21 J14 V18 U20 Y20 W22 C22 Y22 N18 V22 W20"),
            IOStandard("SSTL-15 CLASS I")),
        Subsignal("ba",    Pins("D19 W19 F19"), IOStandard("SSTL-15 CLASS I")),
        Subsignal("cas_n", Pins("E20"), IOStandard("SSTL-15 CLASS I")),
        Subsignal("cke",   Pins("B22"), IOStandard("SSTL-15 CLASS I")),
        Subsignal("clk_n", Pins("E18"), IOStandard("DIFFERENTIAL 1.5-V SSTL CLASS I")),
        Subsignal("clk_p", Pins("D18"), IOStandard("DIFFERENTIAL 1.5-V SSTL CLASS I")),
        Subsignal("cs_n",  Pins("F22"), IOStandard("SSTL-15 CLASS I")),
        Subsignal("dm",    Pins("N19 J15"), IOStandard("SSTL-15 CLASS I")),
        Subsignal("dq", Pins(
            "L20 L19 L18 M15 M18 M14 M20 N20",
            "K19 K18 J18 K20 H18 J20 H20 H19"),
            IOStandard("SSTL-15 CLASS I"),
            Misc("IN_TERM=UNTUNED_SPLIT_40")),
        Subsignal("dqs_n", Pins("L15 K15"),
            IOStandard("DIFFERENTIAL 1.5-V SSTL CLASS I"),
            Misc("IN_TERM=UNTUNED_SPLIT_40")),
        Subsignal("dqs_p", Pins("L14 K14"),
            IOStandard("DIFFERENTIAL 1.5-V SSTL CLASS I"),
            Misc("IN_TERM=UNTUNED_SPLIT_40")),
        Subsignal("odt",   Pins("G22"), IOStandard("SSTL-15 CLASS I")),
        Subsignal("ras_n", Pins("D22"), IOStandard("SSTL-15 CLASS I")),
        Subsignal("reset_n", Pins("U19"), IOStandard("SSTL-15 CLASS I")),
        Subsignal("we_n",  Pins("E22"), IOStandard("SSTL-15 CLASS I")),
        Misc("SLEW=FAST"),
    ),

    # Flash
    # P12 V4 V5 P10 R12 R10 W10 # TODO 3.3-V

    # RGMII Ethernet
    ("eth_clocks", 0,
        Subsignal("tx", Pins("T5")),
        Subsignal("rx", Pins("T6")),
        IOStandard("2.5-V LVTTL")
    ),
    ("eth", 0,
        Subsignal("tx_en",   Pins("P3"), IOStandard("2.5-V LVTTL")),
        Subsignal("tx_data", Pins("U2 W1 N9 W2"), IOStandard("2.5-V LVTTL")), #4
        Subsignal("rx_dv",   Pins("P4"), IOStandard("2.5-V LVTTL")),
        Subsignal("rx_er",   Pins("V1"), IOStandard("2.5-V LVTTL")),
        Subsignal("rx_data", Pins("U5 U4 R7 P8"), IOStandard("2.5-V LVTTL")), #4
#        Subsignal("tx_er",   Pins("")),
        Subsignal("rst_n",   Pins("R3"), IOStandard("2.5-V LVTTL")),
        Subsignal("mdio",    Pins("N8"), IOStandard("2.5-V LVTTL")),
        Subsignal("mdc",     Pins("R5"), IOStandard("2.5-V LVTTL")),
        Subsignal("col",     Pins("R4"), IOStandard("2.5-V LVTTL")),
        Subsignal("crs",     Pins("P5"), IOStandard("2.5-V LVTTL")),
        Subsignal("pcf_en",  Pins("V9"), IOStandard("3.3-V LVTTL")), ## ??? 
        Misc("SLEW=FAST"),
    ),


    # HDMI
    # C18 D17 C17 C19 D14 B19 D13 A19 C14 A17 B16 C15 # D0-D11
    # A14 A15 A12 A16 A13 C16 C12 B17 B12 B14 A18 C13 # D12-D23
    # A20 C9 B11 C11 B10 C10 B15 A7 A10 D12 A9 A11 
    # A8 B8 # TODO 1.8-V

    # USB OTG
    # E12 E13 H13 E14 H14 D15 E15 F15 # D0-7
    # H12 J13 J12 J11 E16 H11 D8 # TODO

    # MIPI
    # R2 R1 N1 P1 T2 T1 N2 N3 # D0-3
    # N5 N4 # diff 2.5-V
    # A4 A3 C3 C2 B1 B2 B3 A2 E11 E10 # 1.2-V
    # T3 U3 U1 V3 M1 M2 # TODO # 2.5-V

    # light sensor i2c
    # Y8 & AA8 (SCL & SDA) # 3.3-V

    # humidity sensor i2c
    # Y10 & AA10 (SCL & SDA) & AB9 (data ready) # 3.3-V

    # temperature sensor SPI/microwire
    # AA1 Y2 AB4  # 3.3-V

    # Accelerometer
    ("acc", 0,
        Subsignal("mosi", Pins("C6")), # SDI ?
        Subsignal("miso", Pins("D5")), # SDO ?
        Subsignal("cs_n", Pins("E9")),
        Subsignal("clk",  Pins("B5")),
        Subsignal("int1", Pins("E8")),
        Subsignal("int2", Pins("D7")),
        IOStandard("1.2-V LVTTL")
    ),

    # SDCard
    ("sdcard", 0,
        Subsignal("clk",       Pins("T20"), IOStandard("1.5-V LVTTL")),
        Subsignal("fb_clk",    Pins("R22"), IOStandard("1.5-V LVTTL")), ## ???
        Subsignal("cmd",       Pins("T21"),             Misc("PULLMODE=UP"), IOStandard("1.5-V LVTTL")),
        Subsignal("cmd_dir",   Pins("U22"), IOStandard("1.5-V LVTTL")),
        Subsignal("dat0_dir",  Pins("T22"), IOStandard("1.5-V LVTTL")),
        Subsignal("dat13_dir", Pins("U21"), IOStandard("1.5-V LVTTL")),
        Subsignal("sel",       Pins("P13"), IOStandard("3.3-V LVTTL")), ## ???
        Subsignal("data",      Pins("R18 T18 T19 R20"), Misc("PULLMODE=UP"), IOStandard("1.5-V LVTTL")),
        #Subsignal("cd",        Pins(""), IOStandard("1.5-V LVTTL")),
    ),
]

# Platform -----------------------------------------------------------------------------------------

class Platform(AlteraPlatform):
    default_clk_name   = "max10_clk1_clk50"
    default_clk_period = 1e9/50e6
    create_rbf         = False

    def __init__(self):
        AlteraPlatform.__init__(self, "10M50DAF484C6G", _io)
        self.add_platform_command("set_global_assignment -name FAMILY \"MAX 10\"")
        #self.add_platform_command("set_global_assignment -name ENABLE_CONFIGURATION_PINS OFF")
        #self.add_platform_command("set_global_assignment -name INTERNAL_FLASH_UPDATE_MODE \"SINGLE IMAGE WITH ERAM\"")

    def create_programmer(self):
        return USBBlaster() # cable_name ?

    def do_finalize(self, fragment):
        AlteraPlatform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("adc_clk_10",    loose=True), 1e9/10e6)
        self.add_period_constraint(self.lookup_request("max10_clk1_clk50", 0, loose=True), 1e9/50e6)
        self.add_period_constraint(self.lookup_request("max10_clk2_clk50", 0, loose=True), 1e9/50e6)
