def rating_normalization(matrix):
    normalized_matrix = []
    
    for row in matrix:
        
        non_zero_ratings = [r for r in row if r != 0]
        
        
        if non_zero_ratings:
            user_mean = sum(non_zero_ratings) / len(non_zero_ratings)
        else:
            user_mean = 0
            
        
        new_row = []
        for r in row:
            if r == 0:
                new_row.append(0.0)
            else:
                # Subtract mean from the original rating
                new_row.append(float(r - user_mean))
        
        normalized_matrix.append(new_row)
        
    return normalized_matrix