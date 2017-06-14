#include <iostream>

using namespace std;

void emptyRowAndCols(int **matrix, int row_count, int col_count)
{
	int i, j;
	bool *rows, *cols;

	rows = new bool[row_count];
	cols = new bool[col_count];

	for(i = 0; i < row_count; i++)
	{
		rows[i] = false;
	}

	for(i = 0; i < col_count; i++)
	{
		cols[i] = false;
	}

	for(i = 0; i < row_count; i++)
	{
		for(j = 0; j < col_count; j++)
		{
			if(!matrix[i][j])
			{
				rows[i] = true;
				cols[j] = true;
			}
		}
	}

	for(i = 0; i < row_count; i++)
	{
		for(j = 0; j < col_count; j++)
		{
			if(rows[i] || cols[j])
			{
				matrix[i][j] = 0;
			}			
		}
	}

	delete [] rows;
	delete [] cols;
}

void initMatrix(int **matrix, int rows, int cols)
{
	int i, j;

	for(i = 0; i < rows; i++)
	{
		matrix[i] = new int[cols];
		for(j = 0; j < cols; j++)
			matrix[i][j] = i * cols + j;
	}

	matrix[0][0] = 0;

	if(rows >= 3 && cols >=3 )
	{
		matrix[1][1] = 0; 
	}

	if(rows >= 5 && cols >= 5)
	{
		matrix[4][4] = 0;
	}
}

void printMatrix(int **matrix, int rows, int cols)
{
	int i, j;

	cout << "---- Matrix Size: " << rows << ',' << cols << " ----" << endl;
	for(i = 0; i < rows; i++)
	{
		for(j = 0; j < cols; j++)
		{
			cout << matrix[i][j] << '\t';
		}
		
		cout << endl;
		delete [] matrix[i];
	}
}

int main()
{
	int *matrix1[1];
	int *matrix2[2];
	int *matrix3[3];
	int *matrix4[4];
	int *matrix5[5];
	int *matrix8[8];

	initMatrix(matrix1, 1, 4);
	initMatrix(matrix2, 2, 5);
	initMatrix(matrix3, 3 ,6);
	initMatrix(matrix4, 4, 7);
	initMatrix(matrix5, 5, 8);
	initMatrix(matrix8, 8, 10);

	emptyRowAndCols(matrix1, 1, 4);
	emptyRowAndCols(matrix2, 2, 5);
	emptyRowAndCols(matrix3, 3, 6);
	emptyRowAndCols(matrix4, 4, 7);
	emptyRowAndCols(matrix5, 5, 8);
	emptyRowAndCols(matrix8, 8, 10);

	printMatrix(matrix1, 1, 4);
	printMatrix(matrix2, 2, 5);
	printMatrix(matrix3, 3, 6);
	printMatrix(matrix4, 4, 7);
	printMatrix(matrix5, 5, 8);
	printMatrix(matrix8, 8, 10);

	return 0;
}