class Solution:
    def twoSum(self):
        index_list = []
        nums = [3,2,4]
        target=6
        for data in nums:
            sec=target-data
            if sec in nums:
                index_list.append(nums.index(data))
                index_list.append(nums.index(sec))
                break
        print(index_list)
        return index_list
            

if __name__ == "__main__":

    solution = Solution()
