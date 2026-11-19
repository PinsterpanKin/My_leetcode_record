# Using java stack
class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(')');
            } else if (c == '{') {
                stack.push('}');
            } else if (c == '[') {
                stack.push(']');
            } else if (stack.isEmpty() || stack.pop() != c) {
                return false;
            }
        }
        return stack.isEmpty();
    }
}
# Model a stack using an array
class Solution {
    public boolean isValid(String s) {
        int n = s.length();
        if(n % 2 == 1) {
            return false;
        }
        char[] stack = new char[n / 2 + 1];
        int top = -1;
        for(char c : s.toCharArray()) {
            if(top >= n/2){
                return false;
            }
            if(c == '(' || c == '{' || c == '[') {
                stack[++top] = c;
            } else {
                if(top < 0) {
                    return false;
                }
                char open = stack[top--];
                if((c == ')' && open != '(') || (c == '}' && open != '{') || (c == ']' && open != '[')) {
                    return false;
                }
            }
        }
        return top == -1;
    }
}