#pragma once

template <typename T>
struct Array {
	T* ptr = nullptr;
	int len = 0;

	Array() { 
		ptr = nullptr;  
		len = 0; 
	}

	Array(int N) {
		ptr = new T * [len];
		len = N;
	}

	Array(int N, T tmp) {
		len = N;
		ptr = new T [len];
		for (int i = 0; i < len; ++i)
			ptr[i] = tmp;
	}

	Array(const Array& p) {
		len = p.len;
		ptr = new T [len];
		for (int i = 0; i < len; ++i)
			ptr[i] = p.ptr[i];
	}

	~Array() {
		delete[] ptr;
	}

};
