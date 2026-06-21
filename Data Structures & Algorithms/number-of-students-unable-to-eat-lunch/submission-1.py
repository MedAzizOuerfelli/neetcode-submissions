class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        qSt = deque(students)
        qSn = deque(sandwiches)
        count = 0
        while qSt:
            st, sn = qSt.popleft(), qSn.popleft()
            if st == sn:
                count = 0
                continue
            else:
                count += 1
                if count == len(qSt) + 1:
                    return count 
                else:
                    qSt.append(st)
                    qSn.appendleft(sn)
        return 0
