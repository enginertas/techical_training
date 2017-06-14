#include <iostream>

using namespace std;

class Stream
{
	private:
		int total_count;
		int current_size;
		int window_size;
		int *elements_array;
		int cur_index;

	public:
		Stream(int n)
		{
			if(n <= 0)
				n = 1;

			elements_array = new int[n];
			cur_index = 0;
			total_count = 0;	
			current_size = 0;
			window_size = n;
		}

		~Stream()
		{
			delete [] elements_array;
		}

		void accept(int elem)
		{
			int key;

			if(current_size == window_size)
			{
				total_count -= elements_array[cur_index];
				current_size--;
			}

			elements_array[cur_index] = elem;
			total_count += elem;
			current_size++;

			cur_index++;
			if(cur_index == window_size)
			{
				cur_index = 0;
			}
		}

		float averageLastElements()
		{
			if(!current_size)
			{
				return 0;
			}	

			return (float)total_count/current_size;
		}
};

int main(int argc, char *argv[])
{
	Stream s = Stream(3);
	cout << "---- Stream ----- " << endl;
	cout << "Count 0:" << endl;
	cout << s.averageLastElements() << endl;
	cout << "Count 1:" << endl;
	s.accept(1);
	cout << s.averageLastElements() << endl;
	cout << "Count 2:" << endl;
	s.accept(2);
	cout << s.averageLastElements() << endl;
	cout << "Count 3:" << endl;
	s.accept(3);
	cout << s.averageLastElements() << endl;
	cout << "Count 4:" << endl;
	s.accept(4);
	cout << s.averageLastElements() << endl;
	cout << "Count 5:" << endl;
	s.accept(5);
	cout << s.averageLastElements() << endl;
	cout << "Count 6:" << endl;
	s.accept(6);
	cout << s.averageLastElements() << endl;
	cout << "Count 7:" << endl;
	s.accept(7);
	cout << s.averageLastElements() << endl;
}

