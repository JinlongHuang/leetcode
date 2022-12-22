class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();
        vector<int> diff(n);
        for (int i = 0; i < n; ++i) {
            diff[i] = gas[i] - cost[i];
        }
        
        int sum = 0;
        vector<int> prefix_sum(n);
        for (int i = 0; i < n; ++i) {
            sum += diff[i];
            prefix_sum[i] = sum;
        }

        if (prefix_sum.back() < 0) 
            return -1;
        else
            return (distance(prefix_sum.begin(), min_element(prefix_sum.begin(), prefix_sum.end())) + 1) % n;
    }
};