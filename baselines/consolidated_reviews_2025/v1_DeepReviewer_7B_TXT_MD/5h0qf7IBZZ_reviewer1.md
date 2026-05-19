### Summary

The paper proposes a new knowledge distillation method for language generation models. It proposes to use reverse KLD instead of forward KLD. It also proposes a few techniques to stabilize the training. The proposed method is tested on a range of LLMs, ranging from 120M to 13B parameters. The proposed MiniLLM consistently outperforms the baselines across the board.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

* The proposed method consistently outperforms the baselines across the board. The experiments are extensive, covering a range of LLMs and evaluation metrics.

### Weaknesses

#### Some Related Works


#### comment

 * The proposed method is incremental. It is not clear what the key factors that lead to the performance gain. It would be great if the authors could provide an analysis on this.
* The paper claims that the proposed MiniLLM produces more precise responses. It would be great if the authors could provide some examples to support this claim.

### Suggestions

The paper would benefit from a more thorough investigation into the specific factors contributing to the performance gains of MiniLLM. While the use of reverse KLD is presented as a key differentiator, the paper lacks a detailed ablation study to isolate its impact. For instance, the authors could experiment with different weighting schemes for the single-step decomposition of the reverse KLD, or explore the effect of this decomposition on the training dynamics. Furthermore, it would be valuable to analyze the sensitivity of MiniLLM to the choice of hyperparameters, such as the learning rate and batch size, and how these parameters interact with the reverse KLD objective. A more granular analysis of the training process, perhaps visualizing the loss curves for both forward and reverse KLD, could also provide insights into the method's behavior. Without such analysis, it remains unclear whether the observed improvements are primarily due to the reverse KLD objective, the proposed training stabilization techniques, or a combination of both.

To strengthen the claim of more precise responses, the authors should provide concrete examples that illustrate the differences between MiniLLM and the baseline methods. These examples should focus on scenarios where MiniLLM demonstrates a clear advantage in terms of response quality. For example, the authors could present cases where the baseline models generate responses that are either too verbose, contain factual inaccuracies, or fail to capture the nuances of the input prompt. In contrast, the authors should highlight instances where MiniLLM generates more concise, accurate, and contextually relevant responses. These examples should be carefully selected to highlight the specific strengths of MiniLLM, and should include both quantitative metrics and qualitative analysis. Furthermore, it would be beneficial to analyze the types of errors made by each model, and to discuss the potential reasons for these errors. This would provide a more comprehensive understanding of the strengths and weaknesses of MiniLLM.

Finally, the paper should include a more detailed discussion of the limitations of the proposed method. While the experimental results are promising, it is important to acknowledge the potential shortcomings of MiniLLM. For example, the authors could discuss the computational cost of training MiniLLM, or the potential for overfitting to the training data. It would also be valuable to explore the generalizability of MiniLLM to different datasets and tasks. A thorough discussion of these limitations would provide a more balanced and nuanced view of the proposed method, and would help guide future research in this area.

### Questions

See above.

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
