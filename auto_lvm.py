import os
import time

def increase ():
        size = int(input("\tEnter Size to Increase : "))
        os.system(f"lvextend --size +{size}G /dev/bobby_vg/lv1")
        os.system(f"resize2fs /dev/bobby_vg/lv1")
        print(f"Size Increased Successfully by {size} GB")

def decrease ():
        present = int(input("\tEnter Present Size (Before Reduce) of Disk : "))
        want = int(input("\tEnter Size After Reducing the Disk : "))
        os.system("umount /lv1")
        os.system("e2fsck -f /dev/bobby_vg/lv1")
        os.system(f"resize2fs /dev/bobby_vg/lv1 {want}G")
        os.system(f"lvreduce --size -{present - want}G /dev/bobby_vg/lv1 -f")
        os.system("mount /dev/bobby_vg/lv1 /mount_point")
        print(f"Size Decreased Successfully by {present - want} GB")


def config ():
        disk = input("\tEnter Disk Name : ")
        os.system(f"pvcreate /dev/{disk}")
        time.sleep(3)
        os.system(f"vgcreate bobby_vg /dev/{disk}")
        size = input("\tEnter Size of the Namenode : ")
        os.system(f"lvcreate --size {size}G --name lv1 bobby_vg ")
        os.system("umount /mount_point")
        os.system("rm -rf /mount_point")
        os.system("mkdir /mount_point")
        os.system(f"mkfs.ext4 /dev/bobby_vg/lv1")
        os.system(f"mount /dev/bobby_vg  /mount_point")
        print("Logical Volume Successfully Created by Lvm")

while (True):

        print('\t1. Create the  Logical Volume')
        print('\t2. Increase the Size of Logical Volume')
        print('\t3. Decrease the Size of Logical Volume')
        print('\t4. Exit')
        ch = input('\tEnter Your choice : ')

        if ch == '1':
                config()
        elif ch == '2':
                increase()
        elif ch == '3':
                decrease()
        elif ch == '4':
                exit()
        else:
                print('Invalid Choice. Try Again !!!')
                                                        
