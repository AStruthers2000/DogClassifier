def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing as to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value. See comments above
                     and the previous topic Calculating Results in the class for details
                     on how to calculate the counts and statistics.
    """
    results_stat_dic = dict()

    #number of images
    results_stat_dic["n_images"] = len(results_dic)
    
    #number of images that are of dogs
    results_stat_dic["n_dogs_img"] = len([key for key in results_dic if results_dic[key][3] == 1])
    
    #number of images that are not of dogs
    results_stat_dic["n_notdogs_img"] = len([key for key in results_dic if results_dic[key][3] == 0])
    
    #number of classifier and image labels that match
    results_stat_dic["n_match"] = len([key for key in results_dic if results_dic[key][2] == 1])
    
    #number of correct dog matches (both labels are of dogs)
    results_stat_dic["n_correct_dogs"] = len([key for key in results_dic if results_dic[key][3] == 1 and results_dic[key][4] == 1])
    
    #number of correct non-dog matches (both labels are not of dogs)
    results_stat_dic["n_correct_notdogs"] = len([key for key in results_dic if results_dic[key][3] == 0 and results_dic[key][4] == 0])
    
    #number of correctly classified breeds
    results_stat_dic["n_correct_breed"] = len([key for key in results_dic if results_dic[key][3] == 1 and results_dic[key][2] == 1])
    
    #percent of label and classifier matches (number of matches / number of images) * 100
    results_stat_dic["pct_match"] = (results_stat_dic["n_match"] / results_stat_dic["n_images"]) * 100
    
    #percent of correctly classified dog images (correctly classified dog images / number of dog images) * 100
    results_stat_dic["pct_correct_dogs"] = (results_stat_dic["n_correct_dogs"] / results_stat_dic["n_dogs_img"]) * 100 
    
    #percent of correctly classified dog breeds (correctly classified dog breeds / number of dog images) * 100
    results_stat_dic["pct_correct_breed"] = (results_stat_dic["n_correct_breed"] / results_stat_dic["n_dogs_img"]) * 100
    
    #percent of correctly classified not-dog images (number of correctly classified not dog images / number of not dog images) * 100
    results_stat_dic["pct_correct_notdogs"] = (results_stat_dic["n_correct_notdogs"] / results_stat_dic["n_notdogs_img"]) * 100

    return results_stat_dic
