# OS Lab Assignment-4
## Implementation and Analysis of Disk Scheduling Algorithms

**Course:** Fundamentals of Operating System Lab (ENCA252)  
**Program:** BCA (AI & DS) (Research)  
**University:** K.R. Mangalam University, New Delhi  
**GitHub:** [rakesh4407](https://github.com/rakesh4407)

---

## 📌 Problem Statement

Disk scheduling is an essential function of operating systems that determines the order in which disk I/O requests are serviced. Efficient disk scheduling improves system performance by reducing seek time and increasing throughput.

This assignment implements and analyzes the following disk scheduling algorithms:
- **FCFS** — First Come First Serve
- **SSTF** — Shortest Seek Time First
- **SCAN** — Elevator Algorithm
- **C-SCAN** — Circular SCAN

---

## 📁 File Structure

```
OS-Lab-Assignment-4/
│
└── disk_scheduling.py      # Main Python file with all algorithms
```

---

## ⚙️ Tools & Technology Used

| Tool | Details |
|------|---------|
| Language | Python 3.x |
| Libraries | Built-in only (no external libraries) |
| IDE | VS Code / PyCharm / IDLE |
| OS | Linux / Ubuntu / Windows |

---

## 🧠 Algorithms Implemented

### 1. FCFS — First Come First Serve
- Requests are serviced in the order they arrive
- Simple but can result in high seek time
- No optimization — head moves back and forth

### 2. SSTF — Shortest Seek Time First
- Always picks the request closest to the current head position
- Reduces seek time compared to FCFS
- May cause **starvation** for far-away requests

### 3. SCAN — Elevator Algorithm
- Head moves in one direction servicing requests
- Reverses direction when it reaches the end of the disk
- Balanced performance — no starvation

### 4. C-SCAN — Circular SCAN
- Head moves in one direction only
- Jumps back to cylinder 0 after reaching the end
- Provides **uniform wait time** for all requests

---

## ▶️ How to Run

### On Linux / Ubuntu:
```bash
python3 disk_scheduling.py
```

### On Windows (PowerShell):
```powershell
python disk_scheduling.py
```

---

## 📥 Sample Input

```
Enter initial head position: 53
Enter disk size (total cylinders): 200
Enter disk request queue: 98 183 37 122 14 124 65 67
```

---

## 📤 Sample Output

```
FCFS  (First Come First Serve)
  Head Movement  : 53 → 98 → 183 → 37 → 122 → 14 → 124 → 65 → 67
  Total Seek Time: 640 cylinders

SSTF  (Shortest Seek Time First)
  Head Movement  : 53 → 65 → 67 → 37 → 14 → 98 → 122 → 124 → 183
  Total Seek Time: 236 cylinders

SCAN  (Elevator Algorithm)
  Head Movement  : 53 → 65 → 67 → 98 → 122 → 124 → 183 → 199 → 37 → 14
  Total Seek Time: 331 cylinders

C-SCAN (Circular SCAN)
  Head Movement  : 53 → 65 → 67 → 98 → 122 → 124 → 183 → 199 → 0 → 14 → 37
  Total Seek Time: 382 cylinders
```

---

## 📊 Performance Comparison

| Algorithm | Total Seek Time | Rank |
|-----------|----------------|------|
| SSTF      | 236 cylinders  | #1 ✔️ |
| SCAN      | 331 cylinders  | #2 |
| C-SCAN    | 382 cylinders  | #3 |
| FCFS      | 640 cylinders  | #4 ✘ |

---

## 📝 Conclusion

- **SSTF** gives the minimum seek time but risks starvation
- **SCAN** is the most balanced for real-world use
- **C-SCAN** gives uniform response — best for heavy load systems
- **FCFS** is simplest but least efficient

---

## 🔗 Related Assignments

- [OS-Lab-Assignment-2](https://github.com/rakesh4407/OS-Lab-Assignment-2)
- [OS-Lab-Assignment-3](https://github.com/rakesh4407/OS-Lab-Assignment-3)
- [OS-Lab-Assignment-4](https://github.com/rakesh4407/OS-Lab-Assignment-4)
