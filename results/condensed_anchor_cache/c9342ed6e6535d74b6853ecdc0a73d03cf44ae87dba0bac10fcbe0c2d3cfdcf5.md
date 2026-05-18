- Decision: Accept
- Scores: 6, 8, 6

## Merged Review

### Summary
The paper proposes a 3D-aware blur synthesizer (GeoSyn) for data augmentation in deblurring. It estimates M 3D vector fields per pixel by combining a parametric 2D rigid transformation field with a non-parametric 3D residual field, then reconstructs the blur image via aggregation. The synthesizer enables controllable blur by adjusting these fields without requiring extra data during training. The method aims to generate more realistic blur patterns than 2D-based augmentation by accounting for 3D camera and object motion.

### Strengths
- The motivation is well-founded: improving deblurring performance through data augmentation is cost-effective and the paper directly addresses key challenges by leveraging 3D space.
- The writing and figures clearly illustrate the motivation, methodology, and results; the paper is easy to follow.
- Comprehensive experiments and ablation studies provide strong evidence of the proposed augmentation’s effectiveness in improving deblurring performance, achieving state-of-the-art results.
- The approach is beneficial to related research in blur data augmentation.
- One reviewer (score 8) was notably more positive, highlighting the logical structure, clear presentation, and robust experimental evidence.

### Weaknesses
- **Blur intensity control:** The current method cannot explicitly adjust overall blur intensity (e.g., via exposure time or a blur intensity parameter); the authors should consider adding such controllability.
- **Derivation of projected 3D residual vector:** More details are needed on how this vector is derived.
- **Role of M and blur diversity:** The correlation between the number of sub-frames M and blur diversity is not explored. Visualizations or metrics showing how blur patterns change with M are missing, which could enhance controllability.
- **Sensitivity to displacement field accuracy:** Inaccurate depth or motion estimation may degrade performance. The authors should test robustness by applying random perturbations to the estimated displacement fields during training to see if the deblurring performance is sensitive to motion field accuracy.
- **Generalization across datasets:** The blur synthesis model is trained separately for each dataset, which lessens the claim of better generalization. Cross-dataset experiments (e.g., training on a single dataset like BSD or RealBlur and testing on another) are needed to demonstrate true generalization. Specifically, ID-Blau could have been fairly compared using datasets with blur-sharp video pairs (BSD [1], RBI [2]), and a cross-dataset evaluation between RealBlur and BSD is necessary.
- **Real-world comparisons:** More comparisons on real-world blurred images captured by the authors are required, and it should be clarified whether the compared models already use existing blur augmentation methods.
- **Limitations of motion trajectories:** Motion trajectories are determined independently of image content, which can produce unrealistic results (e.g., part of a car moving left while another part moves right). The method cannot represent motion from shape-changing objects (e.g., folding fingers, blinking eyes). This limits the complexity of real-world blur the augmenter can cover.
- **Computational cost:** The augmentation scheme increases computational burden. The authors should provide quantitative metrics such as latency, GMACs, and memory usage when adopting GeoSyn.
- **Analysis of motion distributions:** A comparison between the distribution of 2D-based motion trajectories (optical flow between sharp and original blur) and 3D-aware vector fields is missing. Visualizing via t-SNE projection would help show whether the augmented blur trajectories align well with real ones.
- **Camera intrinsics estimation:** How camera intrinsics are obtained from a single image is ill-posed; the authors should clarify whether intrinsics are fixed and only the extrinsic scaling factor is optimized.
- **Synthetic dataset consistency check:** For the synthetic dataset, the reverted sharp image (mean of warped sharp sub-frames per Equation 10) should be identical to the original sharp image. The authors should provide quantitative results verifying this.
- **Video deblurring applicability:** It is unclear whether the method can handle video sequences while maintaining temporal consistency, which is important for applications like Apple Live Photos.
- **“Physical” claim is exaggerated:** From a single image, a neural network cannot theoretically disentangle object motion from camera motion; it can only adapt to the motion patterns in the training dataset. Moreover, the synthesized blur image is still 2D and lacks occluded information, making it less “physical” than synthesis methods that use nearby video frames.
- **Insufficient handling of object motion:** The paper does not adequately address blur caused by object motion (no examples of object-motion-dominated blur are shown), raising doubts about the method's physical realism and effectiveness in complex real-world scenarios.