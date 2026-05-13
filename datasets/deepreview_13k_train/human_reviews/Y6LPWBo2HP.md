# Infinite-Resolution Integral Noise Warping for Diffusion Models

- Decision: Accept
- Scores: 3, 8, 8, 6

## Abstract
Adapting pretrained image-based diffusion models to generate temporally consistent videos has become an impactful generative modeling research direction.
Training-free noise-space manipulation has proven to be an effective technique, where the challenge is to preserve the Gaussian white noise distribution while adding in temporal consistency.
Recently, \citet{chang2024warped} formulated this problem using an integral noise representation with distribution-preserving guarantees, and proposed an upsampling-based algorithm to compute it. However, while their mathematical formulation is advantageous, the algorithm incurs a high computational cost. 
Through analyzing the limiting-case behavior of their algorithm as the upsampling resolution goes to infinity, we develop an alternative algorithm that, by gathering increments of multiple Brownian bridges, achieves their infinite-resolution accuracy while simultaneously reducing the computational cost by orders of magnitude.
We prove and experimentally validate our theoretical claims, and demonstrate our method's effectiveness in real-world applications. We further show that our method readily extends to the 3-dimensional space.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The topic of the paper is to develop computationally efficient algorithms to use image diffusion models temporally, i.e. for generating consistent videos or solving video inverse problems. The authors innovate on the noise-warping mechanism and they propose a computationally efficient method to transform the noise between frames that preserves the Gaussian prior distribution. The authors experimentally validate their method for video super-resolution and 3-D problems.

### Strengths
1) The paper is very well written and the ideas are presented in a natural way.

2) The method is significantly faster compared to the baseline.

3) The fuzzy variant of the method is very clever: significant computation time is saved and the method is more robust as evaluated in real-world applications.

4) The ideas presented are sound and the Euclidean View offers an alternative way to think about the problem of noise warping that I enjoyed reading about.

### Weaknesses
1) The biggest weakness of this paper is that the experimental results are very weak. I downloaded the supplementary material and looked at the videos; the quality is unsatisfactory. While the proposed method offers more consistency than the existing baselines, it is still very inconsistent. The extent of inconsistency is so high, that I can't think of any applications that would leverage this method. Specifically, the temporal flickering and structural inconsistencies are severe, making the generated videos unsuitable for practical use cases such as video editing or high-quality content generation. The lack of fine-grained control over the temporal coherence is a major limitation.

2) At the same time, I am not very confident that the considered approach is meaningful. It is true that at the moment there are many powerful image diffusion models and not so many video diffusion models. However, the current level of quality of solving inverse problems with image diffusion models appears to be very low, judging from the results of this paper. I am not sure if this is a fundamental limitation of the approach or whether it will be resolved in the future. But also, as time goes by, more and more powerful video diffusion models are becoming available that can be used as priors for solving temporal inverse problems. The reliance on image diffusion models for video tasks introduces inherent limitations in capturing temporal dynamics, which is evident in the poor quality of the generated videos.

3) I believe that one of the reasons the experimental results are not that strong is the equivariance of the network itself. Even if the input noise transformations are properly handled, maybe the network itself does not provide equivariant predictions which could cause the creation of flickering and inconsistencies. This is argued in this work: https://arxiv.org/pdf/2410.16152. The lack of equivariance in the diffusion model could be a significant factor contributing to the observed temporal inconsistencies, even with the proposed noise warping technique. The network's inability to maintain consistent transformations across frames likely exacerbates the flickering and structural artifacts.

4) I also believe that the paper would benefit from more experiments on other inverse problems. Since a pre-trained prior is available, one could experiment with other types of problems such as inpainting or even denoising as the image follows simple geometrical transformations (zoom-in/out, shifts, etc). The current evaluation is limited to super-resolution and 3D problems, which does not fully demonstrate the versatility of the proposed method. Expanding the evaluation to include tasks like inpainting and denoising under geometric transformations would provide a more comprehensive understanding of its capabilities and limitations.

### Questions
See also weaknesses above.

1) The experimental results in the website of the How I Warped Your Noise paper (https://warpyournoise.github.io/), seem of much higher consistency compared to the ones provided in the zip file by the authors. Could the authors comment on this? Were there any reproducibility issues?

2) This [paper](https://arxiv.org/pdf/2410.16152) claims that "white noise is not compatible with the idea of using a generative model to interpolate deformed functions". Could the authors comment on this and the preservation of the Gaussian prior under different transformations?

3) Could the authors investigate if having an equivariant generator improves the experimental results?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposed a different formulation for the "integral noise warping" approach of Chang et al. (2024). The authors prove the relation of this formulation (in infinite resolution) to Brownian bridges, and use it to derive novel implementations for the integral noise warping that do not require upsampling, and thus significantly reduce the computational cost of the method proposed by Chang et al. (2024).

### Strengths
- The new interpretation/formulation of integral noise warping is novel and leads to theoretically backed relation to Brownian bridges, whose Markovian property allows to derive convenient implementation methods.

- The derived methods are useful in practical applications where image-based diffusion models are used for video generation in a training-free manner.

- The paper is well-written.

### Weaknesses
 - There is still inconsistency in the details in the frames.  

- The quantitative SDEdit-based video results of the method (and HIWYN) are similar to the competitors.

### Questions
- Since integral noise warping does not prevent noticeable inconsistency in the details in the frames, is it possible to enhance your method by adding an explicit temporal consistency term between frames?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper presents an advanced noise manipulation method to enhance temporal consistency in video generation using diffusion models. The authors address the computational inefficiency in Chang et al.'s (2024) method, which ensures temporal consistency but requires high-resolution upsampling. By shifting from a Lagrangian to an Eulerian perspective and using Brownian bridge increments instead of high-resolution upsampling, the approach achieves the same precision while significantly improving speed and memory efficiency. The author also introduces two methods for calculating noise overlap areas—grid-based and particle-based. The particle-based approach is faster, more memory-efficient, and more robust to non-injective mappings. Results show that this method not only preserves Gaussian noise properties but also achieves speed improvements by several orders of magnitude, maintaining or even improving temporal consistency in video applications, making it more practical for real-world scenarios.

### Strengths
- By using Brownian bridge increments instead of high-resolution upsampling, the proposed method achieves efficient noise manipulation without sacrificing accuracy, greatly enhancing speed and memory efficiency.
- The method maintains temporal consistency of noise in video generation, avoiding flickering or inconsistencies between frames seen in traditional methods, resulting in smoother and more natural video outputs.
- The particle-based noise overlap calculation method is not only faster but also more robust to non-injective mappings, making it suitable for complex, non-linear real-world scenarios and offering high application potential.

### Weaknesses
The symbols are not clearly defined, for example, in the description of the Eulerian Procedure on lines 158-166, $M, m_k, l_k ...$ which can lead to difficulties in reading and understanding.

The ultimate computation goal is the same as in HIWYN: $ \tilde I_{i,j}$ , as shown in Figure 1, the goal is to obtain the "area" of the red region $ \tilde A_{i,j}$ . However, from the Eulerian View, it is evident that $ \tilde A_{i,j} $ will be dispersed across each $ A_{i,j}$ ; in the example in Figure 2, this accounts for 39%. $ I_{i,j}$ can be considered a Brownian bridge from 0 to $ I_{i,j} $, and the area of each deformed region can be viewed as "time." Using this, it might be possible to directly sample the 39% value of the Brownian bridge and then gather it with other red parts across various $ A_{i,j} $ regions to obtain the final $ \tilde A_{i,j}$ . I am not sure if my understanding is correct. If this understanding is correct, then the differently colored regions within $A_{i,j}$ should originate from sampling with different conditions (as indicated by equation (1)), meaning that each color belongs to a different distribution. Would it then be valid to interpret this as an addition of values from Brownian bridges?

### Questions
1. The symbols are not clearly defined, for example, in the description of the Eulerian Procedure on lines 158-166, $M, m_k, l_k ...$ which can lead to difficulties in reading and understanding.

2. The ultimate computation goal is the same as in HIWYN: $ \tilde I_{i,j}$ , as shown in Figure 1, the goal is to obtain the "area" of the red region $ \tilde A_{i,j}$ . However, from the Eulerian View, it is evident that $ \tilde A_{i,j} $ will be dispersed across each $ A_{i,j}$ ; in the example in Figure 2, this accounts for 39%. $ I_{i,j}$ can be considered a Brownian bridge from 0 to $ I_{i,j} $, and the area of each deformed region can be viewed as "time." Using this, it might be possible to directly sample the 39% value of the Brownian bridge and then gather it with other red parts across various $ A_{i,j} $ regions to obtain the final $ \tilde A_{i,j}$ . I am not sure if my understanding is correct. If this understanding is correct, then the differently colored regions within $A_{i,j}$ should originate from sampling with different conditions (as indicated by equation (1)), meaning that each color belongs to a different distribution. Would it then be valid to interpret this as an addition of values from Brownian bridges?

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to tackle the computational inefficiency of the noise warping algorithm first presented by Chang et al. [1]. To this end, the authors propose an Eulerian perspective of the warping problem, which allows achieving equivalent results with orders of magnitude speed-up. The algorithm scatters increments of Brownian bridges from the original pixels to the warped ones, effectively removing the need for a high-resolution sample, as it simulates the case of infinite resolution. Additionally, the paper proposes a particle-based approach which is simpler to implement, more robust and even faster, at the cost of minor loss in accuracy in real-world scenarios. To support the practical value of the proposed method, the authors show applications with video translation tasks and 3D editing.

[1] How I Warped Your Noise: a Temporally-correlated noise prior for diffusion models. (Chang et al.)

### Strengths
1. While the link between noise warping and brownian bridges was noted in previous work, the insights provided by the Eulerian perspective to leverage this connection are novel and theoretically sound.

2. The proposed algorithms greatly improve the computational efficiency of the problem compared to previous work, which can open the door for more potential applications.

3. The particle-based algorithm tackles another limitation of previous work, which was limited to diffeomorphic warpings. This simpler approach can make such method more accessible.

4. The paper is well-written and clear in its explanations, and the proposed method is well validated.

### Weaknesses
1. It is hard to tell from the supplementary video results whether noise warping is actually improving coherency, especially in the 3D case.
2. While the noise warping method is now faster, the authors do not show what practical benefits this speed-up can bring (e.g. what new applications does this open the door to), which slightly hinders the significance of this work.
3. As mentioned by the authors, the method is still limited by the accuracy of the provided flow, and the effects of noise warping in video translation tasks remain based on empirical observations.

### Questions
Not many questions, but I’m curious to know if the authors have any idea what practical use cases could actually benefit from the almost real-time version of noise warping they proposed?

### Soundness
4

### Presentation
4

### Contribution
3
