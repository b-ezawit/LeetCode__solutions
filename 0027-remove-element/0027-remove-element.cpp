class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        vector<int> notValElements;
        int i = 0;

        while (i < nums.size()) {
            if (nums[i] != val) {
                notValElements.push_back(nums[i]);
            }
            i = i + 1;
        }

        int j = 0;
        while (j < notValElements.size()) {
            nums[j] = notValElements[j];
            j = j + 1;
        }

        int originalSize = nums.size();
        int newSize = notValElements.size();
        int difference = originalSize - newSize;

        int counter = 0;
        while (counter < difference) {
            nums[newSize + counter] = val;
            counter = counter + 1;
        }

        return newSize;
    }
};
