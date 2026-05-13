# An Exploration with Entropy Constrained 3D Gaussians for 2D Video Compression

- Decision: Accept
- Scores: 5, 8, 6, 6

## Abstract
3D Gaussian Splatting (3DGS) has witnessed its rapid development in novel view synthesis, which attains high quality reconstruction and real-time rendering. At the same time, there is still a gap before implicit neural representation (INR)  can become a practical compressor due to the lack of stream decoding and real-time frame reconstruction on consumer-grade hardware. It remains a question whether the fast rendering and partial parameter decoding characteristics of 3DGS are applicable to video compression. To address these challenges, we propose a Toast-like Sliding Window (TSW) orthographic projection for converting any 3D Gaussian model into a video representation model. This method efficiently represents video by leveraging temporal redundancy through a sliding window approach. Additionally, the converted model is inherently stream-decodable and offers a higher rendering frame rate compared to INR methods. Building on TSW, we introduce an end-to-end trainable video compression method, GSVC, which employs deformable Gaussian representation and optical flow guidance to capture dynamic content in videos. Experimental results demonstrate that our method effectively transforms a 3D Gaussian model into a practical video compressor.  GSVC further achieves better rate-distortion performance than NeRV on the UVG dataset, while achieving higher frame reconstruction speed (+30%~40% fps) and stream decoding. Code will be released.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper introduces a 2D video compression method using 3D Gaussian Splatting (3DGS), aiming for faster frame reconstruction and stream decoding. However, concerns remain about its limited novelty, as many techniques (e.g., time embeddings, Gaussian attribute adjustments) are adapted from NeRF and 4DGS. The framework largely assembles prior methods (e.g., HAC, GPCC, and optical flow loss from 4DGS) without substantial innovation, raising questions about the applicability and originality of the approach in RGB video compression.

### Strengths
1. Improved Inference Speed:

The compression framework outperforms INR-based inference in rendering speeds, a notable improvement in practical applications where real-time decoding is essential.

2. Broad Performance Evaluation: 

The authors provide comprehensive experiments and comparisons with alternative compression methods, demonstrating that GSVC achieves favorable rate-distortion performance across different quality metrics.

### Weaknesses
1. Lack of Novelty:

The technical novelty of the work is limited. Key techniques, such as time-position embeddings and Gaussian attribute variation over time, have been previously introduced in NeRF and 4DGS [1]. The approach of offsetting Gaussian positions based on features at different timestamps is conceptually similar to the offset extraction in dynamic 4DGS methods. The overall compression framework aligns closely with HAC [2], while the compression of x,y,z coordinates with GPCC was introduced in other prior work. Similarly, optical flow loss is a component already implemented in 4DGS [3]. And the GPU-based ANS ae/ad is already implemented in CompressAI[4].


2. No Comparison with HEVC/VVC:

The paper lacks a direct performance comparison with widely-used standards like HEVC or VVC, making it difficult to gauge its practical effectiveness against traditional video compression methods.


3. Questionable Value for INR/3DGS in RGB Video Compression:

The application of INR/3DGS techniques to RGB video compression seems inherently misaligned with the goals of video compression. Compression frameworks for RGB video typically rely on extensive data to learn a generalized data distribution, leveraging priors that do not exist within a single video or image.

### Questions
Considering the typical aim of RGB image/video compression to leverage extensive priors learned from large datasets, how does the proposed framework add value when applied to compress a single video? Is there any particular benefit in this context?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The authors propose a novel approach to 2D video compression using 3D Gaussian Splatting (3DGS). They represent 2D video sequences as a volumetric distribution in 3D space, using X-Y-T coordinates. To reduce temporal redundancy, they introduce a Toast-like Sliding Window (TSW) projection method that considers Gaussian points within a temporal window centered on the rendering plane. The framework incorporates optical flow information and a FiLM-based deformation field to better capture temporal dynamics. An entropy coding scheme is implemented to optimize model compression and enhance streaming efficiency.

The paper presents three main contributions:
* Introduction of a novel paradigm that represents 2D video using 3D Gaussian models, supported by the TSW projection technique
* Development of GSVC, a comprehensive compression pipeline that combines HAC, deformable fields, and opacity flow regularization
* Experimental validation showing GSVC achieves comparable quality to NeRV while providing 30% faster rendering and flexible bitrate-availability tradeoffs

### Strengths
* Pioneering application of 3DGS to video compression
* Minimal assumptions about video content, relying primarily on temporal continuity, which enables broad applicability
* High adaptability with various 3DGS models, opening promising research directions
* Demonstrated practical utility through flexible bitrate-availability tradeoffs, particularly valuable for streaming applications

### Weaknesses
I do really like the idea of the paper yet the evaluation section could be further polished.
* Limited comparison baseline, with NeRV as the only reference. The evaluation would benefit from comparisons with other neural video compression methods
* Evaluation only focus on low bitrate/bpp scenarios, while contemporary neural compression methods (e.g., VCT, DCVC) typically demonstrate performance at higher bitrates with PSNR values exceeding 34 on the UVG dataset.

### Questions
- In Figure 5, there remains a gap in frame availability even after complete bit decoding. What factors contribute to this limitation?
- Another concern is about the depth sorting when it comes to rendering. there could be a scenario when two gaussians (lets say Ga and Gb), in the frame t-1, fall into Vf, while in the next frame t, they fall into Vb, due to the time plane moving forward. Yet in this case the relative depths of Ga and Gb to the image plane are reversed 
  - for example, in t-1, Ga, Gb in Vf, and Ga is close to the plane, and Gb is further to the plane, then in t, Ga, Gb in Vb, it must be that Ga is further to the plane and Gb looks closer to the plane
  - Such kind of reversing might lead to totally different coloring of the same pixel after alpha blending. has such inconsistency in consecutive frames ever been observed in your experiments?
  - Also how the two images projected from Vb and Vf get mixed into a single image? simply averaging them?
  - It would be interesting if you could visualize the xyt space as a normal 3D space and in the meantime, visualize the rendering of one of the frames from nearby Gaussians. That will be cool.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores 3DGS for video compression. It Introduces TSW projection to adapt 3D Gaussian Splatting for 2D video representation. This paper also develops an end-to-end trainable video compression method based on deformable Gaussian and optical guidance to better model motion content in videos.

### Strengths
1. Orthographic projection and sliding windows for videos are reasonable ideas for adapting the original perspective projection in 3DGS. 

2. Experiments on the UVG dataset show that the developed GSVC codec achieves RD performance compared to NeRV and offers efficient rendering with inherent stream decoding capability. Besides, this paper presents a relatively complete work for the codec workflow. 

3. The paper mentions that the code will be open-source. I appreciate the promise of open source, especially in video compression.

### Weaknesses
1. the proposed method still needs to train per video. Which i think is a limitation for real-world usage. 

2. As video codecs are a well-developed method, this paper does not include comparisons to traditional codecs. I know neural representation for compression is a novel and hot feild. But it’s more valuable and practice to highlight the specific strengths of each methods, especially in terms of the computation costs for encoding.

### Questions
1. Figure 1's ground truth image seems to be with low quality. Based on my knowdege, 3DGS's reconstruct is prune to have high numerical results but lack of details. Have the author consider this issue for compresssion task ?
2. It is hard to see if there is a temporal inconsistency without video examples. Can you provide video comparisons ?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a new framework for video compression from the perspective of 3D Gaussian Splatting (3DGS). The key idea is to construct an interesting spatial-temporal modeling way called toast-like sliding window to cope with the 3D scene modeling in a short time period. This design enables the introduction of several 3DGS-based compression methods into video compression areas. With further careful designs like optical-flow supervision and time-aware Gaussians, the method achieves better compression quality then previous implicit-representation-based approaches like NeRV.

### Strengths
1. The idea of toast-like sliding windows is interesting. It provides an insightful design by treating the time step as an extra dimension to construct a 3D structure.
2. The overall writing is clear and well-motivated. The logical flow is very clear and easy to understand.
3. The overall idea of the exploration of video compression from the 3DGS perspective is novel.

### Weaknesses
1.  Why do toast-like sliding windows need to render a short future period of content? It would be better to provide more illustrations about the detailed rendering process. The current description lacks clarity on how the bi-directional rendering is specifically implemented and how it contributes to the overall compression efficiency. It's unclear how the future frames are used, and what specific information they provide that is not available from past frames. 
2. Ablation study of FiLM design. The analysis of the change from MLP to FiLM-based network structure is missing. The paper does not provide sufficient justification for the choice of FiLM layers over a standard MLP. A detailed comparison of the performance and computational cost between these two architectures is needed to validate the design choice.
3. It would be better to include a more comprehensive comparison of video compression approaches like H.264/265 and HNeRV for in-depth analysis. The current comparison is limited, and a more thorough analysis against established codecs like H.264/265 is necessary to contextualize the performance of the proposed method. The comparison should include a wider range of bitrates and quality metrics.
4.  There are several typos in the writing like line 243, us-> use.

### Questions
1. It would be better to provide the rasterization process when applying the Orthographic Projection in the context of Gaussian Splatting. Including these changes in the appendix will help the readers understand the paper more clearly.
2. How the anchor points are selected in the toast-like sliding windows?

### Soundness
3

### Presentation
3

### Contribution
3
