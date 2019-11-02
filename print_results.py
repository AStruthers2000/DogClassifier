def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
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
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """
    print("\n==========\nHere are the results using the {0} CNN model architechture".format(model))
    
    print("\tThere were {0} images".format(results_stats_dic["n_images"]))
    print("\tOf these images, {0} were images of dogs, whereas {1} were not images of dogs".format(results_stats_dic["n_dogs_img"], results_stats_dic["n_notdogs_img"]))
    
    print("\tThe classifier resulted in {0}% correctly recognized dogs".format(results_stats_dic["pct_correct_dogs"]))
    print("\tThe classifier resulted in {0}% correctly classified breed of dog".format(results_stats_dic["pct_correct_breed"]))
    print("\tThe classifier resulted in {0}% correctly recognized non-dogs".format(results_stats_dic["pct_correct_notdogs"]))
    
    if print_incorrect_dogs:
        print("\nHere are the misclassified dogs (image label and classifier label are in disagreement on if the image is a dog)")
        incorrect_dogs_count = 0
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                incorrect_dogs_count += 1
                print("\t\tThere is a disagreement between the image label: {0}, and the classifier label:  {1} (filename: {2})".format(results_dic[key][0], results_dic[key][1], key))
        print("----There were {0} disagreements between image label and classifier label".format(incorrect_dogs_count))
    
    if print_incorrect_breed:
        print("\nHere are the misclassified breeds (image label and classifier are in disagreement on what the breed of dog is)")
        incorrect_breed_count = 0
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                incorrect_breed_count += 1
                print("\tThere was a disagreement between the image label breed: {0}, and the classifier breed: {1} (filename: {2})".format(results_dic[key][0], results_dic[key][1], key))
        print("----There were {0} disagreements between image label and classifier breed".format(incorrect_breed_count))
               
    
    print("==========")
    None
                
