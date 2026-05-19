### Summary

The paper presents an analysis of the coexistence of multiple deep image watermarking methods within the same image. The authors evaluate eight different watermarking methods and demonstrate that coexistence is possible without mutual interference. The paper also introduces ensembling techniques to improve watermarking performance, including strength clipping, error-correcting codes (ECCs), and parallel/series ensembling. Experimental results show that these methods can achieve new trade-offs between capacity, accuracy, robustness, and image quality without retraining.

### Soundness

2

### Presentation

3

### Contribution

2

### Strengths

1. The paper provides a comprehensive analysis of the coexistence of multiple deep image watermarking methods within the same image, addressing a critical issue in the field.
2. The paper introduces ensembling techniques to improve watermarking performance, including strength clipping, error-correcting codes (ECCs), and parallel/series ensembling. These techniques can achieve new trade-offs between capacity, accuracy, robustness, and image quality without retraining.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a theoretical analysis of the coexistence of different watermarking methods, leaving the underlying mechanisms and conditions for successful coexistence unclear.
2. The paper lacks a comprehensive comparison with existing watermarking methods, particularly those that address similar challenges or use similar techniques. The evaluation is limited to a few methods, and it is unclear how the proposed approach performs against state-of-the-art techniques.
3. The paper does not discuss the limitations of the proposed methods, such as the computational overhead of ensembling or the potential impact on image quality for certain types of watermarks. The analysis is limited to PSNR, and other perceptual metrics should be considered.
4. The paper does not provide a clear explanation of the practical implications of the proposed methods, such as how they can be integrated into existing watermarking systems or how they can be used in real-world applications. The paper does not discuss the potential for false positives or false negatives in the coexistence of watermarks.
5. The paper does not provide a detailed analysis of the robustness of the proposed methods against various attacks, such as compression, filtering, and geometric transformations. The evaluation is limited to a few basic attacks, and it is unclear how the proposed approach performs against more sophisticated attacks.

### Suggestions

The paper would benefit significantly from a more rigorous theoretical analysis of the coexistence of watermarking methods. Specifically, the authors should explore the mathematical conditions under which different watermarks can be reliably embedded and decoded without interfering with each other. This could involve analyzing the frequency domain properties of the watermarks and how they interact with each other. For example, if two watermarks are both based on frequency domain manipulations, it is likely that they will interfere with each other. The analysis should also consider the capacity of the image to accommodate multiple watermarks. The authors should provide a theoretical framework for understanding the limits of coexistence and the trade-offs between capacity, accuracy, robustness, and image quality. This theoretical analysis would provide a deeper understanding of the proposed methods and guide future research in this area.

Furthermore, the paper needs a more comprehensive comparison with existing watermarking methods. The authors should compare their approach with state-of-the-art techniques, including both classical and deep learning-based methods. The comparison should include a detailed analysis of the performance of each method in terms of accuracy, robustness, capacity, and image quality. The authors should also discuss the advantages and disadvantages of their approach compared to existing methods. For example, the authors should compare their approach with methods that use spread spectrum techniques or methods that use multiple watermarks in a single image. This would help to position the proposed approach within the existing literature and highlight its unique contributions. The evaluation should also include a wider range of metrics beyond PSNR, such as perceptual metrics like LPIPS or FID, to better assess the impact on image quality.

Finally, the paper should address the practical implications of the proposed methods. The authors should discuss how their methods can be integrated into existing watermarking systems or how they can be used in real-world applications. The paper should also discuss the potential for false positives and false negatives in the coexistence of watermarks. The authors should provide a more detailed analysis of the robustness of the proposed methods against various attacks, such as compression, filtering, and geometric transformations. The evaluation should include a wider range of attacks to better assess the robustness of the proposed methods. The authors should also discuss the computational overhead of ensembling and the potential impact on image quality for different types of watermarks. This would help to understand the practical limitations of the proposed approach.

### Questions

1. What are the theoretical conditions for the coexistence of different watermarking methods? How do the frequency domain properties of the watermarks affect their coexistence?
2. How does the proposed ensembling approach compare to existing methods for combining watermarking techniques? What are the advantages and disadvantages of the proposed approach?
3. What are the limitations of the proposed methods in terms of computational overhead, image quality, and robustness against various attacks?
4. How can the proposed methods be integrated into existing watermarking systems or used in real-world applications?
5. What is the impact of the proposed methods on the quality of the watermarked images, and how does this impact user experience?

### Rating

3

### Confidence

4

**********
