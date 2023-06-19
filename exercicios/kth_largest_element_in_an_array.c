int partition(int* v,int leftIndex, int rightIndex) {

    int valueToCompare = v[rightIndex];
    int j = leftIndex;

    for(int k = leftIndex; k< rightIndex ; k++)
        if(v[k]<=valueToCompare)
        {

            int temporaryValue = v[k];
            v[k] = v[j];
            v[j] = temporaryValue;
            j++;

        }

    int temporaryValue = v[j];
    v[j] = v[rightIndex];
    v[rightIndex] = temporaryValue;

    return j;
}

void quickSelect(int* v, int valueToSort, int leftIndex, int rightIndex) {

	int j = partition(v, leftIndex, rightIndex);

	if(j == valueToSort) return;
	if(j < valueToSort)
		quickSelect(v, valueToSort, j+1, rightIndex);
	else
		quickSelect(v, valueToSort, leftIndex, j-1);

}

int findKthLargest(int* nums, int numsSize, int k) {
    k = numsSize - k;
    quickSelect(nums, k, 0, numsSize - 1);
    return nums[k];
}
