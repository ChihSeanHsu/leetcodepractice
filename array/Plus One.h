static const auto _____ = []()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();


class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1;
        for(int i = digits.size()-1;i>=0;i--){
            digits[i]+=1;
            if(digits[i] == 10) digits[i] = 0;
            else {
                carry=0;
                break;
            }
        }
        if(carry==1)  digits.insert(digits.begin(),1);
        return digits;
    }
};
