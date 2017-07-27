#!/bin/sh

#Mount
mkdir "/media/$ID_PART_ENTRY_UUID"
mount -o ro "$DEVNAME" "/media/$ID_PART_ENTRY_UUID"

#Show free before backup
/opt/show.py Free
/opt/show_df.py

#Do backup
/opt/rsync.py $ID_PART_ENTRY_UUID

#Unmount and clear mount point
umount "$DEVNAME"
rmdir "/media/$ID_PART_ENTRY_UUID"

#Flush cache
sync

#Show free after backup
/opt/show.py Free
/opt/show_df.py

