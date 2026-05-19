### Summary

This paper identifies and quantifies the problem of model-fitting in guidance during diffusion sampling. The authors propose Compress Guidance, which reduces the number of timesteps that involve gradient calculation, thereby addressing the model-fitting issue. The experimental results show that Compress Guidance can improve image quality and diversity while also reducing the required guidance timesteps by nearly 40%.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The authors propose a novel method called Compress Guidance, which addresses the issue of model-fitting in guidance during diffusion sampling. The idea of reducing the number of timesteps that involve gradient calculation is interesting and has the potential to improve the efficiency of diffusion models.
2. The authors provide a detailed analysis of the problem of model-fitting and the proposed solution. The analysis is well-structured and easy to follow.
3. The experimental results show that Compress Guidance can improve image quality and diversity while also reducing the required guidance timesteps by nearly 40%. The results are promising and demonstrate the effectiveness of the proposed method.

### Weaknesses

#### Some Related Works


#### comment

1. The paper is a bit hard to follow. I suggest the authors provide more details about the implementation of the proposed method. For example, how to choose the guidance steps, and how to implement the gradient calculation. The paper lacks specific details on the selection of the guidance steps, which is crucial for reproducibility. It is unclear whether the guidance steps are chosen randomly, based on a fixed schedule, or adaptively. Furthermore, the paper does not provide sufficient information on how the gradient calculation is implemented, particularly in the context of the proposed compression method. It is unclear how the gradients are approximated or computed efficiently, and how this approximation affects the quality of the generated images.
2. The paper lacks a comparison with other state-of-the-art methods. The authors should compare their method with other methods that aim to improve the efficiency of diffusion models. The absence of a comparison with other relevant methods makes it difficult to assess the true contribution of the proposed method. It is unclear whether the proposed method offers a significant improvement over existing techniques in terms of both efficiency and image quality. The paper should include a thorough comparison with other methods that address similar issues, such as adaptive sampling techniques or other gradient approximation methods.
3. The paper does not provide a detailed analysis of the computational cost of the proposed method. The authors should provide a detailed analysis of the computational cost of the proposed method and compare it with other methods. The paper should include a breakdown of the computational cost, including the time and memory requirements, and compare it with other methods. This analysis should also consider the impact of the proposed compression method on the computational cost. It is important to understand how the proposed method affects the overall computational cost of the diffusion model, and whether it offers a significant improvement in terms of efficiency.

### Suggestions

The authors should provide a more detailed explanation of the implementation of the proposed method, including the selection of guidance steps and the implementation of gradient calculation. Specifically, they should clarify whether the guidance steps are chosen randomly, based on a fixed schedule, or adaptively, and provide a rationale for their choice. They should also provide a detailed description of how the gradient calculation is implemented, including the approximation method used and its impact on the quality of the generated images. This should include a discussion of the trade-offs between computational efficiency and image quality. Furthermore, the authors should provide a pseudocode or a detailed algorithm description of the proposed method, which would greatly enhance the clarity and reproducibility of the work. This would allow other researchers to easily implement and build upon the proposed method.

The authors should include a comprehensive comparison with other state-of-the-art methods that aim to improve the efficiency of diffusion models. This comparison should include a quantitative analysis of the performance of the proposed method and other methods in terms of both image quality and computational cost. The authors should also provide a qualitative analysis of the generated images, highlighting the strengths and weaknesses of the proposed method compared to other methods. This comparison should include a discussion of the limitations of the proposed method and the potential areas for future research. The authors should also discuss the specific scenarios where the proposed method is most effective and where it may not be suitable.

The authors should provide a detailed analysis of the computational cost of the proposed method, including the time and memory requirements. This analysis should include a breakdown of the computational cost, including the time and memory requirements for each step of the proposed method. The authors should also compare the computational cost of the proposed method with other methods, and discuss the trade-offs between computational efficiency and image quality. This analysis should also consider the impact of the proposed compression method on the computational cost. The authors should also discuss the potential for further optimization of the proposed method to reduce its computational cost. This analysis should be presented in a clear and concise manner, with all relevant details included.

### Questions

See Weaknesses

### Rating

5: marginally below the acceptance threshold

### Confidence

3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

**********
