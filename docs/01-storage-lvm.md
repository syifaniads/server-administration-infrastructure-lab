# Storage Management with LVM

## Objective
Manage Linux storage flexibly using Physical Volumes (PV), Volume Groups (VG), Logical Volumes (LV), and filesystem resizing.

## Verified workflow

```text
new virtual disk
   ↓
pvcreate
   ↓
vgextend
   ↓
lvextend
   ↓
resize2fs
   ↓
df -h verification
```

The lab first installed Ubuntu Server with LVM, then added an additional virtual disk. The new disk was detected, initialized as a PV, added to the existing VG, and used to expand the LV mounted at `/home`. The filesystem was resized and final capacity verified.

## Operations demonstrated

```bash
sudo fdisk -l
sudo pvcreate /dev/<NEW_DISK>
sudo vgextend <VG_NAME> /dev/<NEW_DISK>
sudo lvextend -l +100%FREE /dev/<VG_NAME>/<LV_NAME>
sudo resize2fs /dev/<VG_NAME>/<LV_NAME>
df -h
```

All device/VG/LV names above are placeholders; use environment-specific discovery before modifying storage.