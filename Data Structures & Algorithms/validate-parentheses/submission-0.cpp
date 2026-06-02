class Solution {
public:
    bool isValid(string s) {
      //create stack
      stack<char> st;

      for (char c : s) {
        // check if opening bracket
        if ( c == '(' || c == '{' || c == '['){
           // push it on the top of the stack
           st.push(c);
        }
        
        else {
        //this is for the scenario where we run out of opening brackets in our stack, which means that we can no longer form valid parentheses
            if ( st.empty()){
                return false;
            }
            char top = st.top();
            st.pop();

            if ( (c == ')' && top != '(')  || (c == '}' && top != '{') || (c == ']' && top != '[') ) {
                return false;
            }
        }
      } 
      return st.empty();
    }
};
