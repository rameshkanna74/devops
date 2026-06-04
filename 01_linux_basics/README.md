# 🚀 Linux SRE Master Guide – Complete Index & Roadmap

**Your Journey: Absolute Zero → MAANG SRE Interview Ready in 6 Months**

---

## 📚 Complete Cheat Sheet Structure

This comprehensive guide is organized into **4 Levels**, each progressively building from foundational concepts to MAANG-interview-ready expertise.

### 🟢 **LEVEL 1: BEGINNER (Days 1–30)**
*Master the foundation. Navigate filesystems, manage files, understand permissions, write your first scripts.*

**File:** `LEVEL_1_BEGINNER.md`

**What You'll Learn:**
1. Navigating the filesystem (`pwd`, `ls`, `cd`, `tree`, `stat`)
2. Reading files (`cat`, `less`, `head`, `tail`, `tac`, `nl`)
3. Creating & destroying (`touch`, `mkdir`, `rm`, `cp`, `mv`, `ln -s`)
4. Basic permissions (`chmod`, `chown`, `chgrp`, octal & symbolic)
5. Getting help (`man`, `help`, `whatis`, `--help`)
6. Bash Basics (shebang, variables, echo, read, if-then, loops)

**Key Outcomes:**
- Navigate any directory and read files confidently
- Manage file permissions and ownership
- Write simple bash scripts with variables and loops
- Use `man` pages to self-educate
- Understand exit codes and basic error handling

**Time Commitment:** 30 days (1-2 hours/day)

---

### 🟡 **LEVEL 2: INTERMEDIATE (Months 1–3)**
*Scale from "finding files" to "analyzing systems". Searching, text processing, process management, archiving, user management.*

**File:** `LEVEL_2_INTERMEDIATE.md`

**What You'll Learn:**
7. Searching files & directories (`find`, `grep`, `locate`, `which`, `whereis`)
8. Text processing & transformation (`cut`, `sort`, `uniq`, `wc`, `tr`, `diff`, `patch`, `awk`, `sed`)
9. Process management & monitoring (`ps aux`, `top`, `htop`, `kill`, `pkill`, `nice`, `renice`, `jobs`, `bg`, `fg`)
10. File archiving & compression (`tar`, `gzip`, `bzip2`, `xz`, `zip`, `7z`)
11. User & group management (`useradd`, `usermod`, `passwd`, `sudoers`)
12. Disk & filesystem management (`df`, `du`, `ncdu`, `lsblk`, `blkid`, `mount`, `umount`, `fstab`)
13. Bash Intermediate (arrays, functions, exit codes, parameter expansion, `set -e -u`, debugging)

**Key Outcomes:**
- Find anything on the system (`find`, `grep`, `awk`)
- Process text at scale without loading into memory
- Monitor and control running processes
- Back up systems and manage disk space
- Create and manage users with proper permissions
- Write scripts that fail gracefully with error handling

**Time Commitment:** 12 weeks (2-3 hours/day)

---

### 🟠 **LEVEL 3: ADVANCED (Pre-SRE Base)**
*Debug the kernel. Trace syscalls, master systemd, troubleshoot networks, manage storage internals, scale bash.*

**File:** `LEVEL_3_ADVANCED.md`

**What You'll Learn:**
14. Deep process & performance inspection (`strace`, `ltrace`, `lsof`, `fuser`, `/proc`, `sar`, `vmstat`, `iostat`, `pidstat`)
15. SystemD mastery (`systemctl`, `journalctl`, service files, timers, cgroups)
16. Networking 1 – Diagnosis (`ip`, `ss`, `ethtool`, `ping`, `mtr`, `traceroute`, `nslookup`, `dig`, `host`)
17. Networking 2 – Troubleshooting & Security (`tcpdump`, `tshark`, `nmap`, `netcat`, `socat`, firewalls)
18. Storage deep dive (`dd`, `resize2fs`, `xfs_growfs`, `mdadm`, LVM, `fio`)
19. Bash advanced (traps, signal handling, file descriptors, process substitution, getopts, locking, `jq`/`yq`)

**Key Outcomes:**
- Debug any application issue using `strace`/`ltrace`
- Create custom systemd services with proper logging
- Diagnose and fix networking issues at every layer
- Manage LVM and RAID; benchmark disk performance
- Write production bash scripts with proper error handling and JSON/YAML parsing
- Inspect running processes at the kernel level using `/proc`

**Time Commitment:** 12 weeks (3-4 hours/day)

---

### 🔴 **LEVEL 4: SRE GOD MODE (MAANG Interview Ready)**
*Kernel internals, eBPF observability, containers at the metal, production war stories.*

**File:** `LEVEL_4_SRE_GODMODE.md`

**What You'll Learn:**
20. Kernel & hardcore tuning (`sysctl`, `dmesg`, `modprobe`, `lsmod`, `perf`, eBPF basics)
21. Containers & namespaces from the metal (`unshare`, `nsenter`, `cgexec`, cgroups, OCI hooks)
22. Observability on a shoestring (`opensnoop`, `execsnoop`, `biolatency`, `tcpretrans`, `bpftrace`)
23. Bash as a production language (`curl`, `jq`, `yq`, templating, `parallel`, retry logic)
24. Linux SRE scenario challenges (CPU spike → CLOSE_WAIT → fork bomb; diagnosis & fixes)

**Key Outcomes:**
- Tune kernel for production workloads (TCP stack, file descriptors, memory)
- Perform observability 10-100x faster than traditional tools (eBPF)
- Debug containerized applications at the kernel level
- Handle any production incident methodically (CPU, memory, disk, network, service)
- Write production bash that orchestrates deployments, health checks, monitoring
- Interview at Google/Meta/Amazon/Apple as an SRE confidently

**Time Commitment:** 2-4 weeks intensive (4-6 hours/day)

---

## 🗺️ Quick Navigation

### By Task (What Do You Need to Do?)

#### 📍 **Find Things**
- Quick file search: **Level 1** → `find`, `ls`
- Powerful pattern search: **Level 2** → `find`, `grep`, `locate`
- System-wide inspection: **Level 3** → `strace`, `lsof`, `/proc`

#### 📊 **Monitor Performance**
- Real-time processes: **Level 2** → `top`, `htop`, `ps aux`
- System bottlenecks: **Level 3** → `sar`, `vmstat`, `iostat`, `pidstat`
- Kernel hotspots: **Level 4** → `perf`, `opensnoop`, `bpftrace`

#### 🔧 **Manage Storage**
- Disk space: **Level 1** → `du`, `df`
- Filesystems: **Level 2** → `mount`, `fstab`, `mkfs`
- LVM/RAID: **Level 3** → `pvcreate`, `mdadm`, `lvextend`

#### 🌐 **Network Troubleshooting**
- Connection testing: **Level 2** → `ping`, `telnet`
- DNS diagnosis: **Level 3** → `dig`, `nslookup`, `trace`
- Packet capture: **Level 3** → `tcpdump`, `tshark`, firewalls
- Port analysis: **Level 3** → `ss`, `lsof`, `netcat`

#### ⚙️ **System Administration**
- User management: **Level 2** → `useradd`, `sudoers`
- Service management: **Level 3** → systemd, `journalctl`
- Kernel tuning: **Level 4** → `sysctl`, `modprobe`, parameters

#### 🐚 **Scripting & Automation**
- Basic scripts: **Level 1** → variables, loops, if-then
- Robust scripts: **Level 2** → functions, error handling, `&&`/`||`
- Production scripts: **Level 3** → traps, locking, advanced bash
- Enterprise scripts: **Level 4** → JSON/YAML parsing, parallel execution, retries

---

## 📅 6-Month Learning Path

### **Month 1: Foundation (Level 1)**
- **Week 1:** Filesystem navigation, file reading/writing
- **Week 2:** Permissions, ownership, help system
- **Week 3:** First bash scripts (variables, loops, if-then)
- **Week 4:** Practical project: automate daily tasks in bash

---

### **Month 2-3: Intermediate (Level 2)**
- **Week 5:** Finding things (`find`, `grep`, `awk`)
- **Week 6:** Text processing at scale
- **Week 7:** Process management, archiving
- **Week 8:** Disk management, user administration
- **Week 9:** Practical project: write deployment automation script
- **Week 10:** Intermediate bash (arrays, functions, error handling)
- **Week 11-12:** Consolidate; practice on real systems

---

### **Month 4-5: Advanced (Level 3)**
- **Week 13:** Process tracing (`strace`, `ltrace`, `/proc`)
- **Week 14:** SystemD mastery
- **Week 15:** Networking diagnosis and troubleshooting
- **Week 16:** Storage internals, LVM, performance
- **Week 17:** Advanced bash (traps, JSON/YAML, locking)
- **Week 18:** Practical project: debug a slow application, optimize a system
- **Week 19:** Networking from application to kernel layer
- **Week 20-21:** Consolidate; practice incident response scenarios

---

### **Month 6: SRE God Mode (Level 4)**
- **Week 22:** Kernel tuning, eBPF observability
- **Week 23:** Container internals, namespaces
- **Week 24:** Production scenarios: diagnose and fix CPU/memory/disk/network issues
- **Week 25:** Mock interviews, real incident walkthroughs
- **Week 26:** Polish, final projects, interview preparation

---

## 🎯 Interview Preparation

### FAANG SRE Typical Questions & Where to Learn

| Question | Level | File | Topic |
|----------|-------|------|-------|
| "What happens when you run `ls -la`?" | 1 | LEVEL_1 | Filesystem permissions, syscalls |
| "How do you debug a memory leak?" | 2-3 | LEVEL_2/3 | Process monitoring, `pidstat`, profiling |
| "Walk me through a network timeout issue" | 3-4 | LEVEL_3/4 | Networking, DNS, `tcpdump`, `systemd` |
| "Design a deployment script with rollback" | 2-3 | LEVEL_2/3 | Bash, error handling, systemd |
| "How would you diagnose a slow disk?" | 3 | LEVEL_3 | `iostat`, `pidstat`, LVM, performance |
| "Explain container isolation" | 4 | LEVEL_4 | Namespaces, cgroups, `unshare` |
| "Debug a CPU spike in production" | 4 | LEVEL_4 | `perf`, eBPF, `opensnoop`, flame graphs |
| "How do you handle a fork bomb?" | 3-4 | LEVEL_3/4 | Process limits, `pkill`, `ulimit` |
| "Walk me through fixing an OOM issue" | 3-4 | LEVEL_3/4 | Memory pressure, `dmesg`, cgroups |

---

## 💾 Quick Reference by Command

### Alphabetical Command Index

| Command | Level | File | Use Case |
|---------|-------|------|----------|
| `awk` | 2 | LEVEL_2 | Text processing, columnar data |
| `biolatency` | 4 | LEVEL_4 | Disk I/O latency analysis |
| `blkid` | 2 | LEVEL_2 | Show block device UUIDs |
| `cd` | 1 | LEVEL_1 | Change directory |
| `chmod` | 1 | LEVEL_1 | Change permissions |
| `chown` | 1 | LEVEL_1 | Change ownership |
| `cp` | 1 | LEVEL_1 | Copy files |
| `curl` | 4 | LEVEL_4 | HTTP requests, API calls |
| `cut` | 2 | LEVEL_2 | Extract columns |
| `dd` | 3 | LEVEL_3 | Disk cloning, raw I/O |
| `df` | 2 | LEVEL_2 | Disk space by filesystem |
| `dig` | 3 | LEVEL_3 | DNS lookup |
| `dmesg` | 4 | LEVEL_4 | Kernel messages |
| `du` | 2 | LEVEL_2 | Disk usage by directory |
| `ethtool` | 3 | LEVEL_3 | NIC statistics |
| `execsnoop` | 4 | LEVEL_4 | Trace process execution |
| `find` | 2 | LEVEL_2 | Find files |
| `fio` | 3 | LEVEL_3 | Disk I/O benchmark |
| `free` | 2 | LEVEL_2 | Memory usage |
| `grep` | 2 | LEVEL_2 | Search text |
| `groupadd` | 2 | LEVEL_2 | Create group |
| `head` | 1 | LEVEL_1 | First N lines |
| `htop` | 2 | LEVEL_2 | Process monitor (interactive) |
| `iostat` | 3 | LEVEL_3 | Disk I/O statistics |
| `ip` | 3 | LEVEL_3 | Network configuration |
| `iptables` | 3 | LEVEL_3 | Firewall rules |
| `jq` | 4 | LEVEL_4 | JSON parser |
| `journalctl` | 3 | LEVEL_3 | SystemD logs |
| `kill` | 2 | LEVEL_2 | Send signal to process |
| `killall` | 2 | LEVEL_2 | Kill by process name |
| `less` | 1 | LEVEL_1 | Paged file viewer |
| `locate` | 2 | LEVEL_2 | Fast file search (indexed) |
| `lsmod` | 4 | LEVEL_4 | List kernel modules |
| `lsof` | 3 | LEVEL_3 | List open files |
| `ltrace` | 3 | LEVEL_3 | Trace library calls |
| `lvextend` | 3 | LEVEL_3 | Grow logical volume |
| `mkdir` | 1 | LEVEL_1 | Create directory |
| `modprobe` | 4 | LEVEL_4 | Load kernel module |
| `mount` | 2 | LEVEL_2 | Mount filesystem |
| `mtr` | 3 | LEVEL_3 | Trace route (traceroute + ping) |
| `nc` (netcat) | 3 | LEVEL_3 | Network utility |
| `netstat` → `ss` | 3 | LEVEL_3 | Socket statistics |
| `nmap` | 3 | LEVEL_3 | Port scanner |
| `nsenter` | 4 | LEVEL_4 | Enter namespace |
| `nslookup` | 3 | LEVEL_3 | DNS lookup |
| `opensnoop` | 4 | LEVEL_4 | Trace file opens |
| `passwd` | 2 | LEVEL_2 | Change password |
| `perf` | 4 | LEVEL_4 | Performance profiling |
| `pidstat` | 3 | LEVEL_3 | Per-process statistics |
| `ping` | 3 | LEVEL_3 | Test connectivity |
| `pkill` | 2 | LEVEL_2 | Kill by pattern |
| `ps` | 2 | LEVEL_2 | Process snapshot |
| `pwd` | 1 | LEVEL_1 | Print working directory |
| `read` | 1 | LEVEL_1 | Read input |
| `renice` | 2 | LEVEL_2 | Change process priority |
| `resize2fs` | 3 | LEVEL_3 | Grow ext4 filesystem |
| `rm` | 1 | LEVEL_1 | Remove files |
| `sar` | 3 | LEVEL_3 | System activity reporter |
| `sed` | 2 | LEVEL_2 | Stream editor |
| `sort` | 2 | LEVEL_2 | Sort lines |
| `ss` | 3 | LEVEL_3 | Socket statistics |
| `strace` | 3 | LEVEL_3 | Trace syscalls |
| `su` | 2 | LEVEL_2 | Switch user |
| `sudo` | 2 | LEVEL_2 | Execute as root |
| `sysctl` | 4 | LEVEL_4 | Kernel parameters |
| `systemctl` | 3 | LEVEL_3 | SystemD control |
| `tail` | 1 | LEVEL_1 | Last N lines |
| `tar` | 2 | LEVEL_2 | Archive files |
| `tcpdump` | 3 | LEVEL_3 | Packet capture |
| `top` | 2 | LEVEL_2 | Process monitor |
| `touch` | 1 | LEVEL_1 | Create empty file |
| `tr` | 2 | LEVEL_2 | Translate characters |
| `tree` | 1 | LEVEL_1 | Directory tree |
| `unshare` | 4 | LEVEL_4 | Create namespace |
| `useradd` | 2 | LEVEL_2 | Create user |
| `vmstat` | 3 | LEVEL_3 | Virtual memory stats |
| `wc` | 2 | LEVEL_2 | Count lines/words |
| `whatis` | 1 | LEVEL_1 | Command description |
| `which` | 2 | LEVEL_2 | Find command in PATH |
| `yq` | 4 | LEVEL_4 | YAML parser |

---

## 🚨 Emergency Incident Commands (Save These!)

### **CPU Spike? Run This:**
```bash
sudo perf top -K  # Kernel CPU hotspots
pidstat -u 1 5    # Per-process CPU
top -1 -b         # System snapshot
```

### **Out of Memory? Run This:**
```bash
ps aux --sort=-%mem | head
dmesg | tail -20 | grep -i oom
cat /proc/meminfo
```

### **Disk Full? Run This:**
```bash
df -h
du -sh /* | sort -h | tail
lsof | grep REG | wc -l
```

### **Network Down? Run This:**
```bash
ss -tlnp | grep LISTEN
ip addr show
dig @8.8.8.8 example.com
ping 8.8.8.8
```

### **Service Won't Start? Run This:**
```bash
sudo systemctl status myservice
sudo journalctl -u myservice -n 50
sudo strace -f systemctl start myservice
```

---

## 📝 Practice Projects by Level

### **Level 1 Projects**
- [ ] Create a directory structure; organize files with permissions
- [ ] Write a bash script to rename files in batch
- [ ] Set up user accounts with proper permissions

### **Level 2 Projects**
- [ ] Write a bash deployment script (git pull, restart service, verify)
- [ ] Analyze log files (grep, awk, du to find bloated logs)
- [ ] Manage a backup schedule with tar and cron

### **Level 3 Projects**
- [ ] Debug a slow application (strace → lsof → systemd logs)
- [ ] Set up LVM with mirroring and monitoring
- [ ] Create a network monitoring dashboard (ss, sar, systemd)
- [ ] Write a production service file with proper logging

### **Level 4 Projects**
- [ ] Create eBPF one-liners to monitor your system
- [ ] Simulate a production incident (CPU spike) and diagnose it
- [ ] Write a Kubernetes node readiness checker in bash
- [ ] Profile an application and optimize its hotspots

---

## 🏆 Success Criteria by Level

### **Level 1 Complete When:**
- [ ] Navigate any filesystem without help
- [ ] Understand permissions (chmod, chown) intuitively
- [ ] Write bash scripts with variables and loops
- [ ] Use `man` to figure out unfamiliar commands

### **Level 2 Complete When:**
- [ ] Find anything on a system (`find`, `grep`, `awk`)
- [ ] Debug application issues using process tools
- [ ] Manage disks, users, and backups
- [ ] Write reusable utility scripts

### **Level 3 Complete When:**
- [ ] Trace system calls to debug issues
- [ ] Troubleshoot networking at every layer
- [ ] Optimize disk I/O and LVM storage
- [ ] Create production systemd services
- [ ] Write bash that handles errors gracefully

### **Level 4 Complete When:**
- [ ] Profile applications and identify hotspots
- [ ] Debug with eBPF tools (10x faster than strace)
- [ ] Diagnose any production incident methodically
- [ ] Tune kernel for workload requirements
- [ ] Pass FAANG SRE interviews confidently

---

## 🎓 Recommended Study Order

**Option A: Linear (Recommended)**
- Week 1-4: Level 1
- Week 5-16: Level 2
- Week 17-20: Level 3
- Week 21-26: Level 4

**Option B: Accelerated (If you have Linux experience)**
- Week 1-2: Level 1 (quick review)
- Week 3-6: Level 2
- Week 7-16: Level 3
- Week 17-24: Level 4

**Option C: Just-in-Time (If you're interviewing soon)**
- Week 1-2: Skim all levels
- Week 3: Focus on Level 4 scenarios
- Week 4: Mock interviews

---

## 📖 How to Use This Guide

1. **Read the overview** for each level
2. **Study the command tables** (read, don't memorize)
3. **Run every practical example** on a test system
4. **Try the practice projects**
5. **Use the emergency commands** in real situations
6. **Bookmark the quick reference** for daily use

---

## 🤝 Contributing & Feedback

This is a living guide. Found a bug? Missing a command? Have a better example?
Submit issues or PRs to `rameshkanna74/devops` on GitHub.

---

## 📞 Final Advice

> **"The best way to learn Linux is to break it, fix it, and understand why."**
> — Unix Wisdom

Your journey:
1. **Days 1-30:** Explore without fear; breaking is learning
2. **Weeks 5-16:** Focus on depth, not speed
3. **Weeks 17-20:** Connect concepts; see the big picture
4. **Weeks 21-26:** Become the expert; teach others

**You've got this. Go deploy, debug, and dominate.** 🚀

---

**Version:** 1.0  
**Last Updated:** 2026-06-04  
**Platform:** Ubuntu 2024 LTS  
**Created for:** Absolute Beginners → MAANG SRE Interviews
