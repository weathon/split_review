# Tackling the Abstraction and Reasoning Corpus with Vision Transformers: the Importance of 2D Representation, Positions, and Objects

- Decision: Reject
- Scores: 5, 5, 5, 8

## Abstract
\vspace{-1mm}
The Abstraction and Reasoning Corpus (ARC) is a popular benchmark focused on \textit{visual reasoning} in the evaluation of Artificial Intelligence systems. In its original framing, an ARC task requires solving a program synthesis problem over small 2D images using a few input-output training pairs. In this work, we adopt the recently popular \textit{data-driven} approach to the ARC and ask whether a Vision Transformer (ViT) can learn the implicit mapping, from input image to output image, that underlies the task.  We show that a ViT---otherwise a state-of-the-art model for images---fails dramatically on most ARC tasks even when trained on one million examples per task. This points to an inherent representational deficiency of the ViT architecture that makes it incapable of uncovering the simple structured mappings underlying the ARC tasks. Building on these insights, we propose~\method{}, a ViT-style architecture that unlocks some of the visual reasoning capabilities required by the ARC.  Specifically, we use a pixel-level input representation, design a spatially-aware tokenization scheme, and introduce a novel object-based positional encoding that leverages automatic segmentation, among other enhancements. 
Our task-specific~\method{} models achieve a test solve rate close to 100\% on more than half of the $400$ public ARC tasks strictly through supervised learning from input-output grids.
This calls attention to the importance of imbuing the powerful (Vision) Transformer with the correct inductive biases for abstract visual reasoning that are critical even when the training data is plentiful and the mapping is noise-free. Hence, \method{} provides a strong foundation for future research in visual reasoning using transformer-based architectures.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper studies vision transformer in abstract visual reasoning ARC tasks which do not include any text or background knowledge, and focus purely on visual abstraction and pattern recognition. However, directly training a ViT with one million examples per task fails on most ARC tasks. Then, several techniques are proposed to improve model performances, including improved 2D positional encodings, and object-based positional encoding. This work highlights the importance of positional information for utilizing Vision Transformers in visual reasoning tasks.

### Strengths
1. The Abstract Visual Reasoning (AVR) tasks is interesting and important to study because it requires strong reasoning capability of ViTs. The paper also has very interesting findings, highlighting the importance of positional encodings in solving pure vision-based visual reasoning tasks.
2. This works provides very detailed model improvements they have tried to improve the performance, from ViT-Vanilla to ViTARC-VT and ViTARC. This is very useful to the communities to reproduce the experiments and improve further.
3. The final model ViTARC achieves very strong performance in most of the tasks, which is also a significant improvement over ViT-Vanilla.

### Weaknesses
1. The training/evaluation protocol is not clearly defined. The paper does not show clearly the generalization ability on unseen tasks. All the task they use for evaluation have some training examples during training. It would be very interesting to use some tasks pure for evaluation which are not seen during training.
2. Some of the key techniques used in this work are not new, like 2D (Relative) Positional Encoding, which have been discussed in the original ViT/Swin Transformer papers and plays a key role for performance improvement in this work. Though some new techniques are introduced in this work, like Positional Encoding Mixer (PEmixer) and Object-based Positional Encoding (OPE), the overall contribution and novelty is marginal.



### Questions
1. In figure 7, ViTARC-VT has very large variance in terms of performance. Any reason for it? Also what is the key technique leading to the significant performance improvement from ViT-Vanilla to ViTARC-VT? BorderTokens does not look to be important from this figure. Is this because of the 2D positional encodings in ViTARC-VT, instead of 1D positional encodings in ViT-Vanilla?
2. The Equation (12) is not quite clear. I did not find how to calculate the value of $r_{left}$ and $r_{right}$.
3. It is unclear how to tune the hyper-parameters $\alpha$ and $\beta$ in Equation (10), and no ablation studies are provided.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the ARC benchmark from a vision perspective, and answers the question of what changes are required in current SOTA vision architectures to deal with the tasks in ARC. 

The paper suggests that the bad results of vanilla ViTs on these tasks are due to their poor encoding of spatial and positional information, and proposes approaches to deal with this limitation.

Finally, the paper shows results that indicate that the proposed changes were useful for the performance on the ARC benchmark.

### Strengths
1 - The paper addresses an interesting question, which is: if the tasks in ARC are visual tasks, how can se use the current vision tools to deal with them? 

2 - The reasoning behind every contribution in the paper is well explained. The paper is easy to follow. 

3 - Related to the previous point, I particularly like the analysis in Figure 6. It helps understand what the model is (not) paying attention to.

4 - The results in the paper show a clear improvement with respect to the original ViT vanilla baseline, meaning the proposed contributions, overall, are helpful.

### Weaknesses
The paper has some weaknesses that I believe can be addressed, but also should be addressed.

**1 - Unclear that this is vision modeling**.

The main argument of the paper is that vision transformers should be improved to work on ARC. But the proposed changes make the model not be a vision model anymore. While the paper mentions that "Transformer-based LLM approaches convert the images into strings, which does not fully capture all relevant structural information”, this is not too different from what this paper does.
  - By construction, vanilla Transformers model inputs as sequences, but there are some aspects that make them more "vision" specific. Some of them are not included in the original ViT (e.g. local attention), and the others (e.g. patching) are removed in this paper (see next points). A non-Transformer-based architecture (e.g. a U-Net in a diffusion model) would make the connection to vision more clear. (I'm not suggesting such a model should be used, just exemplifying the point).
  - The pixels are encoded in a 1x1 grid, effectively making it a sequence.
  - There is an end-of-sequence token, just as there would be if the task was modeled as a sequence.
  - Even object positional encodings are added, abstracting away the low-level vision from the tasks.

An emphasis on vision is given in the paper more than once, e.g. "However, in vision tasks, especially those requiring detailed visual reasoning, spatial relationships often carry as much importance as, if not more than, the content of the tokens". I believe, however, that a lot of the learned lessons are not about vision, but about structured predictions. In general vision tasks, for example, the content of tokens *is* more important than the spatial relationships.


**2 - Unclear significance of contributions**.

Overall, the paper reads as a sequence of contributions the authors tried, one after another, and building on the previous one, without any global understanding of the problems. I believe the process to get to a solution should not be part of the paper. The paper should just present the final results and justify them. This makes the presentation confusing, for example when showing results in section 4, before going back to explaining some more technical contributions in section 5.

But the main problem is not about presentation. I believe there is some disconnect between the different contributions. Some of the latter ones should make the former ones unnecessary, and these are not ablated properly. The following are some examples:

  - First, learnable embeddings are removed in favor of positional embeddings. But then a PEmixer is necessary to learn position-specific embeddings. And also, RPE is required because APE encodes spatial changes very slowly. All of this is confusing. I believe the paper should directly start by explaining the final encoding and its reasoning, not present two different encoding techniques before the final one and show how they are not ideal.
  - The paper presents quantitative results showing that PEmixer and OPE, on top of ViTARC-VT actually *decrease* the performance of the model.
  - The padding is added at the beginning, but then it results in problems that need to be corrected. I address this in more detail in the next weakness.

**3 - It is unclear that all the padding contributions are necessary**.

Why are padding tokens necessary? The original formulation (sequential padding at the end), where the padding tokens are ignored by the attention should be the correct one (computationally it also makes more sense). The per-row padding (without being attended to) is effectively the same as the per-sequence padding, so I am not sure why it is being mentioned.

I understand that there is a problem about the output not understanding boundaries corrected. But the per-row EOS tokens should be enough to address this issue. For the model, it should be equally hard to predict an "end of row" token than it is to predict the current _<arc endxgrid>_ token. Would it be possible to ablate this? This is another example of weakness #2. The final solution should not include previous iterations of the solution, if these are not necessary. No (attended-to) padding would imply: 
  - More efficient forward and backward passes.
  - No need for three different kinds of end-of-grid tokens. Only a single one would be enough.

**4 - No baselines or comparisons**.

There are no baselines or comparisons to other approaches, only to their own vanilla ViT.  Also, I could not find the paper's performance on the private set of the ARC benchmark, so it is hard to compare to SOTA approaches. Specially interesting comparisons would be to approaches that model ARC as a sequence using an LLM, as I believe the approaches are not very different (see weakness #1).

---

Other minor weaknesses:

- Figure 8 Appendix A seems to motivate the first main technical contributions of the paper. It should not be in the appendix.

- It is unclear why the PEMixer is helping. If every example in the task has different coordinates that are important, I don't understand why it would learn a global (across all samples) weighing. What would be the benefit of giving one position more weight than another one, if every example has different important positions?

- The paper could contain more clarifications and ablations. See "Questions" section.

### Questions
1 - Did you try using RoPE embeddings instead of RPE, in the second point of Section 5? I am curious about the differences.

2 - About RPE: the paper mentions there is an encoding for left and above, and another one for right and below. How are "above and to the right" patches encoded? Why not using an explicit "above left", "above right", "bottom left", "bottom right"? It seems like the approach is re-using the 1D sequential approach without taking into account that we are modeling 2D inputs.

3 - How do your architectural changes influence other vision tasks? E.g. classification, detection, VQA, etc. The SOTA ViT models are nowadays used for many tasks (at least as part of many tasks as vision encoders). It would be great if the changes proposed in the paper did not hurt performance in other tasks.

4 - Related to previous question, did you try starting from a pre-trained ViT?

5 - Did you try training jointly for all tasks? Adding a task ID as context for example.

6 - Did you notice any overfitting or underfitting on the final models? Any scaling properties with the data? On the final models, is 1M samples necessary, of 100k would be enough? Would the models perform better with even more samples?

7 - When generating pixels, during evaluation does the pixel value have to be exact? Is the prediction done as a classification in the RGB [256 x 256 x 256] space? Or is it a regression in the [0-1](x3) range? If it is a regression, how is the correctness evaluated?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors focus on a data-driven model to solve ARC. They first establish that vanilla ViTs fail on ARC despite being trained on a million examples. They then show that a 2D visual representation with ViT improves performance, and that object-based positional information further yields significant performance gains on ARC.

### Strengths
I appreciate that the authors explore the limits of a data-driven approach to ARC, as well as propose potential inductive biases to encode into a reasoning model for ARC. General priors for reasoning tasks are indeed important. The quantitative results compared to a naive ViT are promising for ARC.

### Weaknesses
1. Many of the architectural designs in the proposed model are made for solving ARC specifically. I believe ARC is a great intermediate proxy task for complex reasoning, but should not be an end goal in and of itself. With enough inductive biases, I believe that solving ARC with a million examples is reasonable, but is not particularly enlightening for the community. For example, 2D padding with <arc_pad> tokens and border tokens <arc endxgrid> that define grid conditions, etc, are very much defined for ARC itself.  Would like to see if this model generalizes to other reasoning tasks, for example Raven's progressive matrices, odd one out challenges, etc.
2. In addition, I'm not convinced that these are indeed the best inductive biases. For example, I believe that by using a "2D template" indicated by padding, border, and new-line tokens, the method is endowed with a priori knowledge of what the final grid shape should look like (and also, what the initial grid shape looks like). One core challenge of ARC is precisely that it needs to infer what the output dimensions are (how the shape transforms). Giving the model knowledge that one token should represent one block in ARC is a strong prior to be injecting. 
3. The object-based positional encodings based on OpenCV's contour detections will struggle on more complex or different shapes. This “objectness” should be captured by the visual tokens implicitly. 
4. No other baselines than ViT are explored, though there have been many works proposed for ARC & related reasoning tasks.

### Questions
1. Can you show that the model works on other complex reasoning tasks outside of ARC as mentioned in point 1 above?
2. Does the model work without strong priors, e.g., on input and output grid shape?
3. Can you add in more baselines trained on the same amount of data?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper studies the ARC benchmark, assessing the potential of ViTs for this task when trained with supervision on a single task at a time with plenty of (procedurally-generated) data (which is different from the original few-shot setting).

The paper first shows that standard ViTs fail. It then shows several modifications to the architecture that make them perform much better.

### Strengths
- The paper studies a popular architecture (ViTs), so it should be of broad interest.

- The paper shows a domain where ViTs fail dramatically. The task itself is not interesting (ARC in a new, supervised, large-data setting), but the finding is interesting because it points at intrinsic deficiencies of ViTs.

- Several modifications are described that improve the performance. It's kindof the opposite of an ablation study, but it does the job of demonstrating that novel methods imbue ViTs with novel capabilities.

### Weaknesses
I don't see significant flaws in this paper. Potential weaknesses:

- (W1) The proposed modifications (in particular the visual tokens) are quite straightforward. This can be seen a good thing. I am actually surprised that the absolute PE and padding (to handle images of different sizes or aspect ratios) have not been used before. Are the authors certain this hasn't been described in the existing literature?

- (W2) There is a valid argument that this paper solves a task that is extremely uninteresting in itself. It has no analogue in the real world and it completely defeats the purpose of the original ARC challenge (because of the supervised, large-data setting, focusing on a single task at a time). This paper makes absolutely no progress towards the goal of the ARC challenge. I still think that the findings are interesting for the reasons mentioned in my "Summary" above, i.e. that the proposed improvements give ViTs new abilities. The main issue now is that the contributions of this paper will only have value if/when the abilities are demonstrated to be useful for another task/setting.

### Questions
What do the authors think about adding a caveat in the paper about W2 above? (i.e. the fact that this makes zero progress on the ARC challenge, and that the benefits of the proposed methods still need to be demonstrated on a meaningful task)

I can't solve Task A (6e02f1e3) in Fig. 2. I guess other readers would benefit from an explanation? (I'm afraid this sortof makes a Vanilla ViT superhuman on this task!)

### Soundness
3

### Presentation
3

### Contribution
3
