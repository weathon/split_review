### Summary

The paper proposes a method to identify the domain of a black-box image classifier. The method is based on iteratively generating images from a text-to-image model, classifying them using the black-box classifier, and updating the text prompt to generate more images that are classified as a specific class. The method is evaluated on several datasets and shows promising results.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

- The paper proposes a novel method to identify the domain of a black-box image classifier.
- The method is based on iteratively generating images from a text-to-image model, classifying them using the black-box classifier, and updating the text prompt to generate more images that are classified as a specific class.
- The method is evaluated on several datasets and shows promising results.

### Weaknesses

#### Some Related Works


#### comment

 - The method relies on the quality of the text-to-image model and the black-box classifier. If the models are not accurate or robust, the method may not work well.
- The method may be computationally expensive, as it requires generating and classifying many images.
- The method may not be able to identify the domain of a classifier that is trained on a very specific or unusual dataset.
- The method may not be able to identify the domain of a classifier that is trained on a very small dataset.
- The method may not be able to identify the domain of a classifier that is trained on a dataset that is not well-represented by text prompts.

### Suggestions

The paper's reliance on the text-to-image model's ability to generate diverse and representative images is a significant limitation. The method's success hinges on the assumption that the text prompts can effectively guide the image generation process to cover the full spectrum of the target domain. If the text-to-image model struggles to generate images that accurately reflect the nuances of the target class, the iterative refinement process will likely converge to a suboptimal solution. For example, if the target class is 'birds with long beaks,' the text-to-image model might generate images with beaks that are too short or too long, or with other irrelevant variations. This could lead to the method misidentifying the domain or failing to converge at all. Future work should explore methods to mitigate this dependency, perhaps by incorporating feedback from the black-box classifier directly into the text prompt optimization process, or by using a more robust image generation model that is less sensitive to prompt variations.

Furthermore, the computational cost of the proposed method is a practical concern. The iterative process of generating and classifying many images can be time-consuming and resource-intensive, especially when dealing with large datasets or complex classifiers. The paper should provide a more detailed analysis of the computational complexity of the method and explore potential optimizations to reduce the computational burden. For instance, the authors could investigate techniques to reduce the number of images generated in each iteration, or to use more efficient image classification methods. Additionally, the paper should discuss the scalability of the method to larger datasets and more complex classifiers. It would be beneficial to provide a breakdown of the time spent on each step of the process, such as image generation, image classification, and prompt optimization, to better understand the computational bottlenecks.

Finally, the method's limitations in identifying the domain of classifiers trained on very specific, unusual, or small datasets are significant. The method's reliance on text prompts may not be sufficient to capture the full complexity of such datasets. For example, a classifier trained on a dataset of rare medical images or satellite images of a specific geographic region may not be well-represented by text prompts. The method may also struggle with datasets that are not well-represented by text prompts, such as datasets of abstract art or music. Future work should explore methods to address these limitations, perhaps by incorporating additional information about the dataset or by using a different approach to domain identification that is less reliant on text prompts. It would be beneficial to evaluate the method on a wider range of datasets, including those that are more challenging, to better understand its limitations and potential for improvement.

### Questions

- How does the method perform on datasets with a large number of classes?
- How does the method perform on datasets with a small number of images per class?
- How does the method perform on datasets with a large number of images per class?
- How does the method perform on datasets with a small number of classes and a small number of images per class?
- How does the method perform on datasets with a small number of classes and a large number of images per class?
- How does the method perform on datasets with a large number of classes and a small number of images per class?
- How does the method perform on datasets with a large number of classes and a large number of images per class?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
