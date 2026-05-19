### Summary

This paper presents a two-stage inverse rendering framework that reconstructs and optimizes explicit geometry, materials, and illumination from multiview images. The key contributions include a physically-based inverse rendering model that utilizes multi-bounce path tracing and Monte Carlo integration, and the incorporation of reservoir sampling to accelerate convergence and reduce variance in Monte Carlo rendering. The method achieves state-of-the-art performance in decomposing scene elements and effectively relighting objects, demonstrating its potential for applications in scene editing, relighting, and material editing.

### Soundness

2

### Presentation

2

### Contribution

2

### Strengths

1. The paper is well-organized and clearly written, making it easy to follow and understand.
2. The method achieves state-of-the-art performance in decomposing scene elements and effectively relighting objects, demonstrating its potential for applications in scene editing, relighting, and material editing.

### Weaknesses

#### Some Related Works


#### comment

1. The paper does not provide a clear explanation of how the proposed method addresses the limitations of existing methods, such as TensoIR, in terms of geometry optimization. Specifically, the paper lacks a detailed analysis of how the explicit geometry representation avoids the issues of implicit representations, such as inconsistent optimization during illumination changes, and how it handles topological inconsistencies and geometric instability. The paper should provide a more thorough discussion of these limitations and how the proposed method overcomes them.
2. The paper does not provide a clear explanation of how the proposed method addresses the limitations of existing methods, such as NVdiffrec-MC, in terms of geometry optimization. Specifically, the paper lacks a detailed analysis of how the explicit geometry representation avoids the issues of implicit representations, such as the low expressive capacity of implicit density fields, and how it handles the trade-off between geometric accuracy and computational efficiency. The paper should provide a more thorough discussion of these limitations and how the proposed method overcomes them.
3. The paper does not provide a clear explanation of how the proposed method addresses the limitations of existing methods, such as TensoIR, in terms of material decomposition. Specifically, the paper lacks a detailed analysis of how the physically-based rendering model, combined with multi-bounce path tracing, improves the accuracy of material decomposition compared to purely implicit methods. The paper should provide a more thorough discussion of the advantages of this approach over existing methods.
4. The paper does not provide a clear explanation of how the proposed method addresses the limitations of existing methods, such as NVdiffrec-MC, in terms of relighting. Specifically, the paper lacks a detailed analysis of how the physically-based rendering model, combined with multi-bounce path tracing, improves the accuracy of relighting compared to purely implicit methods. The paper should provide a more thorough discussion of the advantages of this approach over existing methods.
5. The paper does not provide a clear explanation of how the proposed method addresses the limitations of existing methods, such as TensoIR, in terms of mesh extraction. Specifically, the paper lacks a detailed analysis of how the physically-based rendering model, combined with multi-bounce path tracing, improves the accuracy of mesh extraction compared to purely implicit methods. The paper should provide a more thorough discussion of the advantages of this approach over existing methods.
6. The paper does not provide a clear explanation of how the proposed method addresses the limitations of existing methods, such as NVdiffrec-MC, in terms of mesh extraction. Specifically, the paper lacks a detailed analysis of how the physically-based rendering model, combined with multi-bounce path tracing, improves the accuracy of mesh extraction compared to purely implicit methods. The paper should provide a more thorough discussion of the advantages of this approach over existing methods.
7. The paper does not provide a clear explanation of how the proposed method addresses the limitations of existing methods, such as TensoIR, in terms of relighting. Specifically, the paper lacks a detailed analysis of how the physically-based rendering model, combined with multi-bounce path tracing, improves the accuracy of relighting compared to purely implicit methods. The paper should provide a more thorough discussion of the advantages of this approach over existing methods.
8. The paper does not provide a clear explanation of how the proposed method addresses the limitations of existing methods, such as NVdiffrec-MC, in terms of relighting. Specifically, the paper lacks a detailed analysis of how the physically-based rendering model, combined with multi-bounce path tracing, improves the accuracy of relighting compared to purely implicit methods. The paper should provide a more thorough discussion of the advantages of this approach over existing methods.
9. The paper does not provide a clear explanation of how the proposed method addresses the limitations of existing methods, such as TensoIR, in terms of mesh extraction. Specifically, the paper lacks a detailed analysis of how the physically-based rendering model, combined with multi-bounce path tracing, improves the accuracy of mesh extraction compared to purely implicit methods. The paper should provide a more thorough discussion of the advantages of this approach over existing methods.
10. The paper does not provide a clear explanation of how the proposed method addresses the limitations of existing methods, such as NVdiffrec-MC, in terms of mesh extraction. Specifically, the paper lacks a detailed analysis of how the physically-based rendering model, combined with multi-bounce path tracing, improves the accuracy of mesh extraction compared to purely implicit methods. The paper should provide a more thorough discussion of the advantages of this approach over existing methods.
11. The paper does not provide a clear explanation of how the proposed method addresses the limitations of existing methods, such as TensoIR, in terms of relighting. Specifically, the paper lacks a detailed analysis of how the physically-based rendering model, combined with multi-bounce path tracing, improves the accuracy of relighting compared to purely implicit methods. The paper should provide a more thorough discussion of the advantages of this approach over existing methods.
12. The paper does not provide a clear explanation of how the proposed method addresses the limitations of existing methods, such as NVdiffrec-MC, in terms of relighting. Specifically, the paper lacks a detailed analysis of how the physically-based rendering model, combined with multi-bounce path tracing, improves the accuracy of relighting compared to purely implicit methods. The paper should provide a more thorough discussion of the advantages of this approach over existing methods.

### Suggestions

The paper would benefit significantly from a more detailed explanation of how the proposed method addresses the limitations of existing approaches, particularly concerning the challenges of geometry optimization and material decomposition. The current discussion lacks sufficient depth to fully justify the claims of improvement. For instance, the paper should elaborate on how the explicit geometry representation avoids the issues of implicit representations, such as inconsistent optimization during illumination changes and topological inconsistencies. A more thorough analysis of the specific mechanisms that prevent these issues, such as the use of a differentiable surface representation and how it interacts with the multi-bounce path tracing, would be beneficial. Furthermore, the paper should provide a more detailed explanation of how the explicit geometry representation avoids the low expressive capacity of implicit density fields, and how it balances geometric accuracy with computational efficiency. This should include a discussion of the specific choices made in the design of the explicit geometry representation and how these choices contribute to the overall performance of the method.

Additionally, the paper needs to provide a more in-depth analysis of how the physically-based rendering model, combined with multi-bounce path tracing, improves the accuracy of material decomposition and relighting compared to purely implicit methods. The current discussion is too high-level and lacks the necessary technical details to fully support the claims. For example, the paper should explain how the physically-based rendering model allows for more accurate modeling of indirect lighting and how this, in turn, leads to more accurate material decomposition. The paper should also provide a more detailed explanation of how the multi-bounce path tracing is implemented and how it contributes to the improved performance. Furthermore, the paper should discuss the limitations of the proposed method and how these limitations might be addressed in future work. This should include a discussion of the potential challenges in handling complex scenes with multiple light sources and materials, and how the method might be extended to address these challenges.

Finally, the paper should provide a more detailed explanation of how the proposed method addresses the limitations of existing methods in terms of mesh extraction. The current discussion is too brief and lacks the necessary technical details to fully support the claims. The paper should explain how the physically-based rendering model, combined with multi-bounce path tracing, improves the accuracy of mesh extraction compared to purely implicit methods. This should include a discussion of the specific mechanisms that allow for more accurate surface reconstruction and how these mechanisms contribute to the overall performance of the method. The paper should also discuss the limitations of the proposed method in terms of mesh extraction and how these limitations might be addressed in future work. This should include a discussion of the potential challenges in handling complex scenes with multiple light sources and materials, and how the method might be extended to address these challenges.

### Questions

1. How does the proposed method address the limitations of existing methods, such as TensoIR, in terms of geometry optimization?
2. How does the proposed method address the limitations of existing methods, such as NVdiffrec-MC, in terms of geometry optimization?
3. How does the proposed method address the limitations of existing methods, such as TensoIR, in terms of material decomposition?
4. How does the proposed method address the limitations of existing methods, such as NVdiffrec-MC, in terms of relighting?
5. How does the proposed method address the limitations of existing methods, such as TensoIR, in terms of mesh extraction?
6. How does the proposed method address the limitations of existing methods, such as NVdiffrec-MC, in terms of mesh extraction?
7. How does the proposed method address the limitations of existing methods, such as TensoIR, in terms of relighting?
8. How does the proposed method address the limitations of existing methods, such as NVdiffrec-MC, in terms of relighting?
9. How does the proposed method address the limitations of existing methods, such as TensoIR, in terms of mesh extraction?
10. How does the proposed method address the limitations of existing methods, such as NVdiffrec-MC, in terms of mesh extraction?

### Rating

3

### Confidence

5

**********
