#include "cuda_runtime.h"
#include "tools.cuh"
#include "base.cuh"
#include <stdio.h>

#ifdef _DEBUG
#include <iostream>
#endif


#ifdef _DEBUG
template<typename T>
void print(Array<T> arr) {
    for (int i = 0; i < arr.len; ++i) {
        std::cout << arr.ptr[i] << ' ';
    }
}
#endif

int main() {
    printDevicesInformation();
#ifdef _DEBUG
    //printf("%d", 1);
    Array<int> arr(10, 8);
    print(arr);
#endif
    return 0;
}