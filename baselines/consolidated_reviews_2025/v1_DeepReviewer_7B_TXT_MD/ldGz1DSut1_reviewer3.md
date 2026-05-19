### Summary

This paper investigates the coexistence of deep image watermarking methods and introduces a new ensembling technique to improve watermarking performance. The authors evaluate the coexistence of eight different watermarking methods and demonstrate that they can coexist within the same image without mutual interference. They also show how ensembling techniques can increase the overall message capacity and enable new trade-offs between capacity, accuracy, robustness, and image quality without retraining.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-structured and easy to follow.
2. The paper provides a comprehensive analysis of the coexistence of deep image watermarking methods and introduces a new ensembling technique to improve watermarking performance.

### Weaknesses

#### Some Related Works


#### comment

1. The paper lacks a theoretical analysis of the coexistence of different watermarking methods, leaving the underlying mechanisms and conditions for successful coexistence unclear. Specifically, the paper does not delve into the mathematical properties that allow different watermarking schemes to be applied sequentially or in parallel without interference. It would be beneficial to explore the frequency domain characteristics of the watermarks and how they interact, as well as the capacity constraints of the image itself.
2. The paper does not compare the proposed ensembling method with existing watermarking techniques, making it difficult to assess its effectiveness and novelty. The paper should include a comparison with other ensembling techniques used in watermarking or other image processing tasks, such as spread spectrum methods or error correction codes. Without such a comparison, it is hard to determine if the proposed method offers a significant advantage over existing approaches.
3. The paper does not discuss the limitations of the proposed method, such as its computational complexity or its robustness against different types of attacks. The paper should analyze the computational overhead of the ensembling technique, including the encoding and decoding times, and how it scales with the number of watermarking methods being combined. Furthermore, the robustness of the proposed method against various image processing operations, such as compression, noise addition, and geometric transformations, should be evaluated and discussed.
4. The paper does not provide sufficient experimental results to support the claims made in the paper. The experiments should include a more comprehensive evaluation of the proposed method, including a wider range of datasets, watermarking methods, and attack scenarios. The paper should also provide a more detailed analysis of the results, including statistical significance tests and visualizations of the watermarked images.

### Suggestions

To address the lack of theoretical analysis, the authors should explore the mathematical properties of the watermarking methods being coexist. This could involve analyzing the frequency domain characteristics of the watermarks and how they interact with each other. For example, if two watermarks are both based on frequency domain manipulations, it is likely that they will interfere with each other. The authors should also investigate the capacity constraints of the image itself and how the different watermarking methods interact with these constraints. This could involve analyzing the bit rates of the different watermarking methods and how they combine to fill the available capacity of the image. A theoretical framework that explains the conditions under which different watermarking methods can coexist would significantly strengthen the paper.

To better assess the effectiveness and novelty of the proposed ensembling method, the authors should compare it with existing watermarking techniques, including other ensembling methods used in image processing. This comparison should include a quantitative analysis of the performance of the proposed method and other methods in terms of capacity, accuracy, robustness, and image quality. The authors should also discuss the advantages and disadvantages of the proposed method compared to other methods. For example, the authors could compare the computational complexity of the proposed method with other methods, or they could compare its robustness against different types of attacks. This would help to determine if the proposed method offers a significant advantage over existing approaches.

To address the lack of experimental results, the authors should include a more comprehensive evaluation of the proposed method. This should include a wider range of datasets, watermarking methods, and attack scenarios. The authors should also provide a more detailed analysis of the results, including statistical significance tests and visualizations of the watermarked images. For example, the authors could evaluate the performance of the proposed method on different types of images, such as natural images, medical images, and satellite images. They could also evaluate the robustness of the proposed method against different types of attacks, such as compression, noise addition, and geometric transformations. This would help to demonstrate the generalizability and robustness of the proposed method.

### Questions

1. How does the proposed ensembling method affect the computational complexity of the watermarking process?
2. How robust is the proposed method against different types of attacks, such as compression, noise addition, and geometric transformations?
3. What are the limitations of the proposed method in terms of its applicability to different types of images and watermarking scenarios?

### Rating

5

### Confidence

3

**********
