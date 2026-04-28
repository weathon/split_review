# LaMPlace: Learning to Optimize Cross-Stage Metrics in Macro Placement

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
Machine learning techniques have shown great potential in enhancing macro placement, a critical stage in modern chip design.
However, existing methods primarily focus on *online* optimization of *intermediate surrogate metrics* that are available at the current placement stage, rather than directly targeting the *cross-stage metrics*---such as the timing performance---that measure the final chip quality.
This is mainly because of the high computational costs associated with performing post-placement stages for evaluating such metrics, making the *online* optimization impractical.
Consequently, these optimizations struggle to align with actual performance improvements and can even lead to severe manufacturing issues.
To bridge this gap, we propose **LaMPlace**, which **L**earns **a** **M**ask for optimizing cross-stage metrics in macro placement.
Specifically, LaMPlace trains a predictor on *offline* data to estimate these *cross-stage metrics* and then leverages the predictor to quickly generate a mask, i.e., a pixel-level feature map that quantifies the impact of placing a macro in each chip grid location on the design metrics.
This mask essentially acts as a fast evaluator, enabling placement decisions based on *cross-stage metrics* rather than *intermediate surrogate metrics*.
Experiments on commonly used benchmarks demonstrate that LaMPlace significantly improves the chip quality across several key design metrics, achieving an average improvement of 9.6\%, notably 43.0\% and 30.4\% in terms of WNS and TNS, respectively, which are two crucial cross-stage metrics that reflect the final chip quality in terms of the timing performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper presents LaMPlace, a novel machine learning method aimed at enhancing macro placement in chip design by prioritizing cross-stage metrics, such as timing performance, over intermediate metrics. The approach employs an offline-trained predictor to generate a pixel-level mask that evaluates the impact of macro placements on design metrics, followed by a greedy algorithm for placement optimization. Experimental results demonstrate a noteworthy average improvement of 9.6% in chip quality, with significant enhancements of 43.0% in WNS and 30.4% in TNS.

### Strengths
+ The method shows strong zero-shot inference capabilities, allowing for effective generalization to unseen designs without requiring extensive training samples in the offline phase.
+ It successfully optimizes cross-stage metrics, including HPWL, WNS, and TNS, concurrently, which is a significant advancement in macro placement techniques.

### Weaknesses
 - The algorithm struggles with placing macros that are not edge-connected, limiting its effectiveness in scenarios where macros do not have interconnections. This is a significant limitation as many designs include macros with sparse connectivity, and the method's reliance on a graph-based approach may not be suitable for such cases. The lack of explicit handling for isolated macros could lead to suboptimal placements, especially in designs with heterogeneous macro connectivity patterns.


### Questions
- In Figure 9, related to DREAMPlace, there are blank rectangular areas, and some macros appear to overlap. Could you clarify this observation? Additionally, could you provide visualized results for the baseline method?
- The timing-driven option in DREAMPlace does not seem to support macros effectively. Can you present results with this option disabled?
- How does LaMPlace handle macros that are smaller than the grid size?
- Some tables, such as Table 4 and Table 8, are missing units. Could you rectify this oversight?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces LaMPlace, a machine learning-based approach to optimize macro placement in EDA by focusing on cross-stage metrics that impact the final quality of chip designs. Traditional methods often optimize surrogate metrics, which are simpler to compute but do not directly correlate with final chip performance. LaMPlace tackles this by training a predictor to estimate these cross-stage metrics offline and generating a pixel-level mask to inform placement decisions efficiently. This work improved timing performance metrics like WNS and TNS, etc. Experimental results demonstrate that LaMPlace achieves significant improvements, with an average increase of 9.6% across key metrics.

### Strengths
Focus on final metrics and thus improved results: LaMPlace addresses a critical gap by targeting final chip quality metrics rather than intermediate surrogate metrics.

Efficiency: By using a pre-trained predictor, the proposed method reduces the high computational cost associated with evaluating cross-stage metrics during placement.

Zero-shot Generalization: The method demonstrates strong generalization on unseen benchmarks, showing adaptability without extensive fine-tuning.

### Weaknesses
Computational Complexity: Despite its efficiency improvements, the approach still relies on a complex training phase that may limit its practical applications in resource-constrained environments.

Potential Overhead in Prediction: Generating the placement mask may still introduce additional computational overhead, particularly when applied to larger, more complex designs.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work proposes a novel learning-based macro placement algorithm which learn a mask to optimize multiple cross-stage metrics. The performance of this algorithm is significant especially as the timing metrics, i.e., TNS and WNS.

### Strengths
1. The idea of L-flow and L-mask is novel and the improvement is significant.
2. Comprehensive experiment and analysis.

### Weaknesses
Some parts of technical contents and experimental settings should be explained.

1. “Notably, this function is translation-invariant with respect to the macro positions.“ Even if the relative positions of two macros remain unchanged for chip placement, the final design metrics (e.g., congestion and timing) will still change. This is because the macros' positions relative to the chip boundary affect the placement of other standard cells. Therefore, I wonder if there is a more detailed explanation of “translation-invariant”. Specifically, how does the model account for the influence of chip boundaries on the placement of standard cells and the resulting impact on design metrics? It would be helpful to clarify the extent to which this assumption holds and under what conditions it might be violated.
2. More explanation about pair-wise ranking could be included in the paper. The current description lacks sufficient detail regarding the specific implementation of the pair-wise ranking method. For instance, how are pairs of macro placement solutions selected for comparison? What criteria are used to determine the relative ranking of two solutions within a pair? Providing a more comprehensive explanation of the pair-wise ranking process, including the loss function and optimization procedure, would significantly enhance the paper's clarity and reproducibility.
3. The final metric "HPWL" often serves as a surrogate metric in the design flow. "Wirelength" is a common final metric, that most people are concerned with, to replace "HPWL". While HPWL is a useful proxy, it does not directly reflect the actual wirelength after routing. It would be beneficial to include results for post-route wirelength, in addition to HPWL, to provide a more complete evaluation of the proposed method's effectiveness in optimizing the final design quality.

### Questions
Thanks to the authors’ contributions for proposing this novel macro placement algorithm and performing comprehensive experiments. Meanwhile, this paper is well-written and easy to read.

I still have some questions about the technical contents and experimental settings.

1. “Notably, this function is translation-invariant with respect to the macro positions.“ Even if the relative positions of two macros remain unchanged for chip placement, the final design metrics (e.g., congestion and timing) will still change. This is because the macros' positions relative to the chip boundary affect the placement of other standard cells. Therefore, I wonder if there is a more detailed explanation of “translation-invariant”.
2. More explanation about pair-wise ranking could be included in the paper.
3. The final metric "HPWL" often serves as a surrogate metric in the design flow. "Wirelength" is a common final metric, that most people are concerned with, to replace "HPWL".

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper introduces LaMPlace, a novel method for macro placement in chip design that focuses on optimizing cross-stage metrics, such as timing performance, which are crucial for the final chip quality. LaMPlace addresses this by learning a mask that guides the placement process based on cross-stage metrics. The proposed method involves (1) training a predictor on offline data to estimate cross-stage metrics, and (2) using this predictor to generate a mask, which is a pixel-level feature map that quantifies the impact of placing a macro in each chip grid location on the design metrics. This mask enables placement decisions based on cross-stage metrics rather than intermediate surrogate metrics. The paper demonstrates the effectiveness of LaMPlace on commonly used benchmarks, showing improvements in chip quality across several key design metrics, including WNS and TNS.

### Strengths
1. The paper introduces a unique approach to macro placement that directly addresses the optimization of cross-stage metrics, crucial for the final chip quality. Existing methods often focus on optimizing intermediate surrogate metrics, which can lead to sub-optimal chip quality.
2. The proposed method, LaMPlace, has been demonstrated to be effective in improving chip quality across several key design metrics, including WNS and TNS, which are crucial for timing performance. The paper provides great empirical results on commonly used benchmarks, showing significant improvements in chip quality.
3. The use of a mask for placement optimization allows for efficient placement decisions based on cross-stage metrics. It enables the optimization of cross-stage metrics without incurring the high computational costs associated with existing methods.
4. The paper acknowledges the practicality of its approach for industry applications. It emphasizes that the offline setting for training the predictor is feasible due to the availability of substantial chip data from design projects.

### Weaknesses
1. Reliance on Offline Data. The paper's approach hinges on the availability of substantial offline chip data for training the predictor. While the paper argues that this is practical in the industry, it may limit the applicability of the method in scenarios where such data is scarce or unavailable. Specifically, the reliance on pre-existing datasets raises questions about the model's adaptability to entirely new chip architectures or design paradigms not represented in the training data. Addressing this limitation, either through data augmentation techniques or alternative training strategies, would enhance the paper's broader impact. For instance, how well would the model perform when faced with a novel chip design that deviates significantly from the patterns present in the offline dataset?

2. Black-Box Nature of the Predictor. The predictor used in LaMPlace is a black box, meaning its internal workings and decision-making processes are not transparent. This lack of interpretability may make it difficult to understand why certain placement decisions are made, potentially hindering further improvements or debugging of the method. Specifically, did authors find strange examples, which are difficult for human experts to understand? For instance, are there specific macro placements that consistently lead to improved cross-stage metrics but defy conventional design wisdom? An in-depth analysis of such cases could provide valuable insights into the predictor's behavior and potentially reveal novel design principles.

3. Limited Discussion of Scalability. The paper does not explicitly discuss the scalability of LaMPlace to very large-scale designs with millions of cells. While the method shows promising results on the tested benchmarks, further analysis of its computational complexity and memory requirements for larger designs would be beneficial. For example, how does the runtime of the mask generation process scale with the number of macros and the size of the chip grid? Additionally, what are the memory requirements for storing the predictor and the intermediate data structures during the placement process? Providing concrete data on these aspects would strengthen the paper's claims about the practicality of LaMPlace for real-world industrial applications.

### Questions
1. Ablation study on the size of the offline dataset. What are the results with different sizes of offline dataset?
2. The authors claim that they will release the code once the paper is accepted. Is it possible to discuss more implementation details or release the code for review?

### Soundness
3

### Presentation
3

### Contribution
3
