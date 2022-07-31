class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.array = [ [[0, 0]] for i in range(length) ]
        self.curr_ver = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if self.array[index][-1][0] != self.curr_ver:
            # curr ver is not exist
            self.array[index].append([self.curr_ver, val])
        else:
            # curr is exist
            self.array[index][-1][1] = val

    def snap(self):
        """
        :rtype: int
        """
        self.curr_ver += 1
        return self.curr_ver - 1
        

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        binary_search_array = self.array[index]
        size = len(binary_search_array)
        l, r = 0, size - 1
        while l <= r:
            m_index = (l + r) // 2
            if binary_search_array[m_index][0] < snap_id:
                l = m_index + 1
            elif snap_id < binary_search_array[m_index][0]:
                r = m_index - 1
            else:
                return binary_search_array[m_index][1]
        
        # 超出範圍
        if l >= r:
            l = l - 1
        
        return binary_search_array[l][1]

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)

# res = []
# obj = SnapshotArray(4)
# obj.snap()
# obj.snap()
# obj.set(0, 4)
# print(obj.array)
# print(obj.get(0, 1))

res = []
obj = SnapshotArray(4)
res.append('null')

obj.set(1, 5)
res.append('null')

id = obj.snap()
res.append(id)

obj.set(0, 16)
res.append('null')

res.append(obj.snap())

obj.set(2, 15)
res.append('null')

res.append(obj.snap())

obj.set(2, 5)
res.append('null')

res.append(obj.get(1, 0))

res.append(obj.get(0, 2))

res.append(obj.snap())
print(obj.curr_ver)
print(obj.array)
print(res)



# print('set 0,5')
# obj.set(0,5)
# print('snap')
# param_2 = obj.snap()
# print('--return: ' + str(param_2))
# print('set 0,6')
# obj.set(0,6)
# print('get')
# obj.snap()
# param_3 = obj.get(1,0)
# print(param_3)
# print('--return: ' + str(param_3))