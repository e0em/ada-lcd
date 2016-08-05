#!/bin/bash
expect auto_ap_login.exp  |while read line ; do echo "$line" | grep "rb_data" | cut -f 2 -d "=" ; done

