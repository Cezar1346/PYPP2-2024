def spy_game(nums):
    pos_0 = pos_0_found = False
    pos_1 = pos_7 = None

    for num in nums:
        if num == 0:
            if not pos_0_found:
                pos_0 = nums.index(num)
                pos_0_found = True
        elif num == 7:
            if pos_0_found:
                pos_7 = nums.index(num)
                if pos_7 > pos_0:
                    return True
    return False