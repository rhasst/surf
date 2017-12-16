# Load RUCKUS library
source -quiet $::env(RUCKUS_DIR)/vivado_proc.tcl

# Load Source Code
if { $::env(VIVADO_VERSION) >= 2014.4 } {
   loadSource -dir  "$::DIR_PATH/rtl"
} else {
   puts "\n\nWARNING: $::DIR_PATH requires Vivado 2014.4 (or later)\n\n"
}   
