### Summary

This paper studies the coexistence of multiple deep image watermarking methods and proposes an ensembling method to improve the overall message capacity and enable new trade-offs between capacity, accuracy, robustness and image quality. The authors evaluate the coexistence of eight different watermarking methods and demonstrate that they can coexist within the same image without mutual interference. The authors also show how ensembling can increase the overall message capacity and enable new trade-offs between capacity, accuracy, robustness and image quality, without needing to retrain the base models.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-written and easy to follow.
2. The paper provides a comprehensive analysis of the coexistence of deep image watermarking methods and proposes a new ensembling method to improve the overall message capacity and enable new trade-offs between capacity, accuracy, robustness and image quality.
3. The authors provide a detailed analysis of the trade-offs between capacity, accuracy, robustness and image quality, and show how ensembling can enable new trade-offs without needing to retrain the base models.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a theoretical analysis of the coexistence of different watermarking methods. It would be beneficial to provide a theoretical framework for understanding the conditions under which different watermarking methods can coexist without mutual interference. Specifically, the paper does not explore the mathematical properties that allow different watermarking schemes to be applied sequentially or in parallel without affecting each other. This lack of theoretical grounding makes it difficult to generalize the findings beyond the specific methods tested.
2. The paper does not compare the proposed ensembling method with existing watermarking techniques, making it difficult to assess its effectiveness and novelty. The paper should include a comparison with other ensembling techniques used in watermarking or other image processing tasks, such as spread spectrum methods or error correction codes. Without such a comparison, it is hard to determine if the proposed method offers a significant advantage over existing approaches. The paper should also discuss the computational complexity of the proposed ensembling method compared to other techniques.
3. The paper does not discuss the limitations of the proposed method, such as its computational complexity or its robustness against different types of attacks. The paper should analyze the computational overhead of the ensembling technique, including the encoding and decoding times, and how it scales with the number of watermarking methods being combined. Furthermore, the robustness of the proposed method against various image processing operations, such as compression, noise addition, and geometric transformations, should be evaluated and discussed. The paper should also discuss the potential for false positives or false negatives in the coexistence of watermarks.
4. The paper does not provide sufficient experimental results to support the claims made in the paper. The experiments should include a more comprehensive evaluation of the proposed method, including a wider range of datasets, watermarking methods, and attack scenarios. The paper should also provide a more detailed analysis of the results, including statistical significance tests and visualizations of the watermarked images. The paper should also discuss the limitations of the experimental setup and how these limitations might affect the generalizability of the results.

### Suggestions

The paper would benefit significantly from a more rigorous theoretical analysis of the coexistence of watermarking methods. The authors should explore the mathematical properties of the watermarks and the image content to determine the conditions under which different watermarking schemes can be applied without interference. This could involve analyzing the frequency domain characteristics of the watermarks and how they interact with each other. For example, if two watermarks are both based on frequency domain manipulations, it is likely that they will interfere with each other. The authors should also investigate the capacity constraints of the image itself and how the different watermarking methods interact with these constraints. A theoretical framework that explains the conditions under which different watermarking methods can coexist would significantly strengthen the paper and provide a deeper understanding of the proposed approach. This theoretical analysis should be supported by mathematical proofs and derivations.

To better assess the effectiveness and novelty of the proposed ensembling method, the authors should compare it with existing watermarking techniques, including other ensembling methods used in image processing. This comparison should include a quantitative analysis of the performance of the proposed method and other methods in terms of capacity, accuracy, robustness, and image quality. The authors should also discuss the computational complexity of the proposed ensembling method compared to other techniques. For example, the authors should analyze the encoding and decoding times of the proposed method and compare them to the encoding and decoding times of other watermarking techniques. Furthermore, the authors should discuss the robustness of the proposed method against different types of attacks, such as compression, noise addition, and geometric transformations. This comparison should be supported by experimental results and should include a discussion of the limitations of the proposed method.

Finally, the paper needs to include a more comprehensive experimental evaluation of the proposed method. The experiments should include a wider range of datasets, watermarking methods, and attack scenarios. The authors should also provide a more detailed analysis of the results, including statistical significance tests and visualizations of the watermarked images. The paper should also discuss the limitations of the experimental setup and how these limitations might affect the generalizability of the results. For example, the authors should discuss the impact of different image resolutions and bit depths on the performance of the proposed method. The authors should also discuss the limitations of the chosen watermarking methods and how these limitations might affect the generalizability of the results. The experimental results should be presented in a clear and concise manner, with appropriate statistical analysis and visualizations.

### Questions

1. How does the proposed ensembling method affect the computational complexity of the watermarking process?
2. How robust is the proposed method against different types of attacks, such as compression, noise addition, and geometric transformations?
3. What are the limitations of the proposed method in terms of its applicability to different types of images and watermarking scenarios?

### Rating

6

### Confidence

3

**********
