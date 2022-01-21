#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(){
    int listSize;
    cin >> listSize;
    vector<int> originalList;
    vector<int> resultList;

    for (int i = 0; i < listSize; i++){
        int temp;
        cin >> temp;
        originalList.push_back(temp);
    }

    sort(originalList.begin(), originalList.end());

    for (int i = 0; i < listSize; i++){
        if (listSize % 2 == 0 && i == listSize / 2){
            resultList.push_back(originalList[i]);
            resultList.push_back(originalList[listSize - i - 1]);
            break;
        }else if (listSize % 2 != 0 && i == listSize / 2){
            resultList.push_back(originalList[i]);
            break;
        }
        resultList.push_back(originalList[i]);
        resultList.push_back(originalList[listSize - i - 1]);
    }
    
    for (int i = 0; i < listSize; i++){
        if (i == listSize - 1){
            cout << resultList[i] << '\n';
            break;
        }
        cout << resultList[i] << endl;
    }

    return 0;
}


