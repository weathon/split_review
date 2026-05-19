### Summary

The paper investigates the coexistence of multiple deep image watermarking methods within the same image, aiming to enhance robustness and accuracy. It evaluates eight different watermarking methods and demonstrates that coexistence is possible without mutual interference. The paper also introduces ensembling techniques to improve watermarking performance, including strength clipping, error-correcting codes (ECCs), and parallel/series ensembling. Experimental results show that these methods can achieve new trade-offs between capacity, accuracy, robustness, and image quality without retraining.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

- The paper explores the coexistence of multiple watermarking methods within a single image, addressing the growing complexity of digital ecosystems and the need for multiple watermarks in the same image.
- The paper introduces ensembling techniques to improve watermarking performance, including strength clipping, error-correcting codes (ECCs), and parallel/series ensembling, which can achieve new trade-offs between capacity, accuracy, robustness, and image quality without retraining.

### Weaknesses

#### Some Related Works


#### comment

 - The paper does not provide a theoretical analysis of the coexistence of different watermarking methods, leaving the underlying mechanisms and conditions for successful coexistence unclear.
- The paper lacks a comprehensive comparison with existing watermarking methods, particularly those that address similar challenges or use similar techniques. The evaluation is limited to a few methods, and it is unclear how the proposed approach performs against state-of-the-art techniques.
- The paper does not discuss the limitations of the proposed methods, such as the computational overhead of ensembling or the potential impact on image quality for certain types of watermarks. The analysis is limited to PSNR, and other perceptual metrics should be considered.
- The paper does not provide a clear explanation of the practical implications of the proposed methods, such as how they can be integrated into existing watermarking systems or how they can be used in real-world applications. The paper does not discuss the potential for false positives or false negatives in the coexistence of watermarks.
- The paper does not provide a detailed analysis of the robustness of the proposed methods against various attacks, such as compression, filtering, and geometric transformations. The evaluation is limited to a few basic attacks, and it is unclear how the proposed approach performs against more sophisticated attacks.

### Suggestions

The paper should include a more rigorous theoretical analysis of the coexistence of different watermarking methods. This analysis should explore the mathematical conditions under which different watermarks can be reliably embedded and decoded without interfering with each other. The authors should consider the frequency domain properties of the watermarks and how they interact with each other. For example, if two watermarks are both based on frequency domain manipulations, it is likely that they will interfere with each other. The analysis should also consider the capacity of the image to accommodate multiple watermarks. The authors should provide a theoretical framework for understanding the limits of coexistence and the trade-offs between capacity, accuracy, robustness, and image quality. This theoretical analysis would provide a deeper understanding of the proposed methods and guide future research in this area.

The paper needs a more comprehensive comparison with existing watermarking methods. The authors should compare their approach with state-of-the-art techniques, including both classical and deep learning-based methods. The comparison should include a detailed analysis of the performance of each method in terms of accuracy, robustness, capacity, and image quality. The authors should also discuss the advantages and disadvantages of their approach compared to existing methods. For example, the authors should compare their approach with methods that use spread spectrum techniques or methods that use multiple watermarks in a single image. The comparison should also include a discussion of the computational complexity of each method and the resources required to implement them. This would help to position the proposed approach within the existing literature and highlight its unique contributions.

The paper should also discuss the limitations of the proposed methods in more detail. The authors should analyze the computational overhead of ensembling and the potential impact on image quality for different types of watermarks. The authors should also discuss the potential for false positives and false negatives in the coexistence of watermarks. The paper should also include a more comprehensive evaluation of the robustness of the proposed methods against various attacks, such as compression, filtering, and geometric transformations. The evaluation should include a detailed analysis of the performance of each method under different attack conditions. The authors should also discuss the potential for adaptive attacks that are designed to remove or disrupt the coexistence of watermarks. This would help to identify the limitations of the proposed approach and guide future research in this area.

### Questions

- What are the theoretical conditions for the coexistence of different watermarking methods? How do the frequency domain properties of the watermarks affect their coexistence?
- How does the proposed ensembling approach compare to existing methods for combining watermarking techniques? What are the advantages and disadvantages of the proposed approach?
- What are the limitations of the proposed methods in terms of computational overhead, image quality, and robustness against various attacks?
- How can the proposed methods be integrated into existing watermarking systems or used in real-world applications?

### Rating

3

### Confidence

4

**********
