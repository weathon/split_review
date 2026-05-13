# On a Hidden Property in Computational Imaging

- Decision: Reject
- Scores: 5, 3, 6

## Abstract
Computational imaging plays a vital role in various scientific and medical applications, such as Full Waveform Inversion (FWI), Computed Tomography (CT), and Electromagnetic (EM) inversion. These methods address inverse problems by reconstructing physical properties (e.g., the acoustic velocity map in FWI) from measurement data (e.g., seismic waveform data in FWI), where both modalities are governed by complex mathematical equations. In this paper, we empirically demonstrate that despite their differing governing equations, three inverse problems—FWI, CT, and EM inversion—share a hidden property within their latent spaces. Specifically, using FWI as an example, we show that both modalities (the velocity map and seismic waveform data) follow the same set of one-way wave equations in the latent space, yet have distinct initial conditions that are linearly correlated. This suggests that after projection into the latent embedding space, the two modalities correspond to different solutions of the same equation, connected through their initial conditions. Our experiments confirm that this hidden property is consistent across all three imaging problems, providing a novel perspective for understanding these computational imaging tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper considers a hidden property in computational imaging, demonstrated across Full Waveform Inversion (FWI), Computed Tomography (CT), and Electromagnetic (EM) inversion tasks, which reveals that they share a common set of one-way wave equations in the latent space. The authors leverage understanding of this shared latent representation to achieve accurate reconstructions and predictions across imaging tasks, achieving similar or better performance than existing methods but with fewer parameters.

### Strengths
- Results of experiments on computational imaging tasks show simliar or improved performance with fewer model parameters.

### Weaknesses
 - The work draws very heavily on two prior works by Chen et al. 2023 (a,b).  As far as I can tell neither of these works have been accepted by peer-review venues.
- There is no theoretical motivation for the hidden wave equations, as far as I can tell, although I did not review the cited papers.


### Questions
- Can the authors speculate about similarity between the computational imaging tasks considered that might give rise to the observed phenomenon?  Or do they believe this phenomenon should existing for all computational imaging tasks?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper considers three inverse problems (namely, FWI, CT reconstruction, and EM inversion). The authors propose a new architecture for the reconstruction operator by exploiting the relationship between the latent representation of the measured data and the parameters to be reconstructed.  In particular, the construction of the reconstruction net exploits the fact that the data and the parameters, in their latent space, are governed by the same wave equation with linearly correlated initial conditions. Numerical experiments are conducted to demonstrate the performance of the new architecture as compared with a couple of baseline methods for the three inverse problems mentioned above.

### Strengths
The paper proposes an interesting idea to extend FINOLA (first-order norm+linear autoregressive modeling) to consider both the data space and the parameter space. This can potentially lead to useful architectures for various other inverse problems.

### Weaknesses
1. In my opinion, the paper’s main contribution is to propose a new architecture, and not establish any fundamental “hidden property” in computational imaging problems (contrary to what the abstract and the introduction attempt to portray). This also makes the overall presentation somewhat misleading and difficult to follow.

2. The numerical experiments do not provide strong evidence in favor of the proposed method. The baseline methods for comparison (e.g., SIRT and InversionNet for CT) are chosen somewhat arbitrarily. State-of-the-art deep learning methods for CT (such as learned primal-dual by Adler and Oktem) are not used for comparison, making it difficult to judge the empirical superiority of the new architecture.

### Questions
The overall exposition is somewhat difficult to follow, primarily because of the lack of clarity about the paper’s main contributions and the usage of non-standard terminologies in comparison with the inverse problems literature. For instance, the word “modality” is used to refer to the parameter and data spaces, which can lead to confusion. Some specific comments are below:

- Abstract: “where both modalities are governed by complex mathematical equations”: This is a rather vague statement to use in the abstract. What specific governing equations are being referred to here? What latent space is talked about here? The actual contributions or the significance of the proposed method do not come out clearly from the abstract.  

- Figure 1 caption (and other places in the introduction): The phrase “latent space” is used frequently without much explanation about what exactly it refers to. 

- Page 2: “Whether an elegant mathematical relationship exists in the latent space, akin to that
in the original space?”: I don’t think it is a precise, well-formulated research question. The mathematical relationship between the parameter space and the data space is determined by the specific imaging modality, whereas the relationship in the “latent space” is empirically enforced (and no such relationships are shown to exist theoretically). 

- Page 2: “...typically with a bottleneck in the network, they lack a deeper understanding of these latent representations.”: I don’t see any such “deeper understanding” (which in itself is somewhat vague and subjective) being uncovered in this paper either. 

- The phrase “target property” is used in several places in the paper. Could you please explain what this means?

- Section 2.1: It might be good to make the descriptions of the inverse problems (FWI, CT, and EM inversion) more concise. 

- Page 6: “Difference with vanilla FINOLA”: This part needs to be rewritten. Currently, it gives the impression that the proposed method is capable of handling multi-modal data for reconstruction, which it isn’t. 

- Page 7: Architecture details: Do you use the same architecture for the reconstruction network for all three inverse problems considered? 

- CT experiments: There is no comparison with the unrolling-based techniques (such as learned primal-dual), which are known to yield state-of-the-art reconstruction performance. The choice of the baseline techniques is somewhat arbitrary and not well-motivated.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper present a framework for solving inverse problems like the full waveform inversion. The problem is tackled by projecting the data inside an embedding space which linearize the initial condition. Furthermore the proposed method combined a reconstruction and a inversion target and the two embedding spaces are linked using wave equations. Such result is of large interest for the inverse problem community. The framework shows promising results against to state-of-art methods.

### Strengths
The paper presents a very interesting framework for solving a class of inverse problems.

1. **Originality**: while this paper relies on previous recent research, the HINT framework is new. The multi-path FINOLA is clearly a novelty for this problematic. The hidden wave phenomenon is very intriguing and the underling properties seem pretty helpful to inverse. 
2. **Quality**: the method is well motivated and the context is clear. The link with previous work is done with the contribution clearly highlighted.
3. **Clarity**: the paper is easy to read and most of the components are described.
4. **Significance**: since inverse problems are an important class of problems in signal, imaging... such work can have a big impact on the community.

### Weaknesses
There few weakness is the article, they are minor but they impact my final score.

1. The class of inverse problems that can be considered is unclear. Do we have an idea of which problems involved an hidden wave phenomenon? Even an insight would be welcome. Specifically, the paper does not provide a clear characterization of the types of inverse problems where the proposed hidden wave property is expected to hold. It is unclear if this property is specific to certain types of wave equations or if it is a more general phenomenon. A more detailed discussion of the underlying assumptions and limitations of the framework is needed.
2. The multi-path FINOLA need a better description. I don't see the "multipath" in the equations. The description of the multi-path FINOLA is insufficient. The paper does not clearly explain how the multiple paths are implemented and how they contribute to the final solution. The equations provided do not directly show how the multi-path approach is integrated into the framework. A more detailed explanation of the architecture and its relation to the equations is required.
3. One small experiment to compare the method with classical framework (LASSO with wavelets...) would interesting to have a full idea on the effectiveness of the framework. The lack of comparison with classical methods such as LASSO with wavelets makes it difficult to assess the true effectiveness of the proposed framework. While the paper shows promising results, a comparison with well-established methods would provide a more complete picture of the advantages and disadvantages of the proposed approach.

### Questions
* I have a question on the class of inverse problems, do modalities like MRI or tomography enter in the framework?
* Please clarify the part about the multipath.

### Soundness
3

### Presentation
4

### Contribution
3
