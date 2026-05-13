# Contrastive learning of cell state dynamics in response to perturbations

- Decision: Reject
- Scores: 5, 5, 3

## Abstract
We introduce DynaCLR, a self-supervised framework for modeling cell dynamics via contrastive learning of representations of time-lapse datasets. Live cell imaging of cells and organelles is widely used to analyze cellular responses to perturbations. Human annotation of dynamic cell states captured by time-lapse perturbation datasets is laborious and prone to bias. DynaCLR integrates single-cell tracking with time-aware contrastive learning to map images of cells at neighboring time points to neighboring embeddings. Mapping the morphological dynamics of cells to a temporally regularized embedding space makes the annotation, classification, clustering, or interpretation of the cell states more quantitative and efficient. We illustrate the features and applications of DynaCLR with the following experiments: analyzing the kinetics of viral infection in human cells, detecting transient changes in cell morphology due to cell division, and mapping the dynamics of organelles due to viral infection. Models trained with DynaCLR consistently achieve $>95\%$ accuracy for infection state classification, enable the detection of transient cell states and reliably embed unseen experiments. DynaCLR provides a flexible framework for comparative analysis of cell state dynamics due to perturbations, such as infection, gene knockouts, and drugs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors present a self-supervised framework for leveraging contrastive learning to model cell state dynamics from time-lapse imaging. 
The model allows temporally adjacent states to be mapped closely together helping achieve accurate, efficient, and label-free analysis of dynamic cell states under perturbations like viral infection. The paper presents a unique application of contrastive learning in cellular imaging and stands out for its temporal coherence and robustness in infection state classification.

### Strengths
- The use of temporally-aware contrastive learning enables efficient modeling of time-dependent cellular changes, showing improved performance over traditional contrastive methods, especially under perturbative conditions.
- The framework facilitates rapid annotation of cell states, potentially decreasing the reliance on human-intensive and subjective labeling, a significant advancement over prior approaches.
- By using a cell-aware approach, the framework attempts to address the intrinsic heterogeneity across cell populations, an advantage over traditional time-agnostic contrastive approaches.

### Weaknesses
- The choice of a 30-minute interval as the temporal offset might not generalize across other biological systems with different dynamics, limiting the model adaptability.
- The reliance on phase and fluorescence imaging could constrain its utility where alternate modalities are necessary.
- Since cell-aware and time-aware sampling use specific tracked cells, the embeddings may risk overfitting to individual cell trajectories instead of generalized dynamics.
- Although contrastive learning was chosen, the paper lacks in-depth comparisons with generative methods that authors summarize in the related work.
- By setting a fixed temporal offset, the model may miss capturing events that unfold asynchronously or at variable rates in different cells.
- Models relying on phase channels for cell division detection may struggle with subtler morphological changes that require fluorescence markers.

### Questions
- How does the model perform for other tasks beyond infection classification? Like, for example, tracking mitotic spindle dynamics during first cell division in embryonic development? 

- How does the model handle potential noise or artifacts in the time-lapse imaging data? How are hyperparameters tuned and how sensitive is the model to the choice of these hyperparameters?

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
3

### Summary
In this paper, the authors propose a framework for modeling cell dynamics in response to perturbations. They suggested several downstream tasks for the learned representation, such as the analysis of viral infection kinetics in human cells, detecting transient changes in cell morphology, and mapping organelle dynamics due to viral infection. Furthermore, they reported that the proposed framework achieves an accuracy of over 95% for infection state classification, outperforming the supervised setting.

### Strengths
- The paper is well-written, following a clear structure that enhances readability and comprehension.
- The learned representation was used in several dowstream tasks.

### Weaknesses
- The technical novelty of the paper is limited, as DynaCLR may be considered a straightforward application of the triplet loss with varied sampling strategies.
-  Some figures (Fig. 2, Fig. 3, and Fig. 6) are not thoroughly explained; a more detailed description would enhance clarity.

### Questions
- The choice of the triplet loss is not justified. Why is this loss more suitable for this task than alternatives like NT-Xent or InfoNCE?
- In Section 4.1.1, could you clarify ithe origin of the independent test data?
- In Section 4.2, the smooth transitions and tight clustering of division events are not immediately evident in Figure 4; additional support for these claims would be beneficial.
- In Section 4.3, it remains unclear how the referenced figures demonstrate that "the encoder learns meaningful features that describe cell dynamics."
- Figure 6 would benefit from a more detailed explanation.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper describes an application of contrastive learning on a microscopy dataset to model single cell dynamics. The method introduces time-aware sampling to the traditional contrastive learning methodology by making use of cell-tracking. Three downstream applications of the learned embeddings are shown which demonstrate how the method can be used to analyze cell-state dynamics in response to perturbations. In addition, experiments showing generalization and interpretability of embeddings are performed.

### Strengths
1.	The paper addresses an interesting topic where self-supervised learning has the potential to be extremely beneficial. Getting annotations for large amounts of microscopy data on a single-cell level is difficult and there is a broad push in the field towards the kind of self-supervised approach described here, so this work is well placed.
2.	The utilization of cell tracking to improve self-supervised learning is an interesting idea; cell-identity detection is potentially a useful proxy task that could aid in learning good representations.
3.	The biological setup and experiments are well thought out and the dataset would be beneficial to researchers as a benchmark, given simple readouts like infection rate.
4.	The addition of generalization experiments (though only on one additional set of data) provides some grounding to the results – without this section I don’t think the paper has much weight. I would encourage the authors to extend this to more datasets if possible.

### Weaknesses
1.	In general, this is written like a paper in a scientific journal rather than a machine learning conference. While it is important to provide the necessary biological context, the paper lacks the mathematical discourse required to be suitable in a machine-learning setting. For example, could you add a theoretical or mathematical description of ideas such as ‘smoothness’ or ‘richness’ of the latent space that you have mentioned?  
2.	I’m not quite sure that the quantitative results match up with the claims made. For example, performance scores in Table 1 are better for the ‘classical’ contrastive learning approach as opposed to the ‘cell-aware’ and ‘time-aware’ approaches. The arguments made based on the Euclidean distance plots in Figure 2 are strenuous, and I don’t agree with the qualitative conclusions made about time-regularized contrastive learning being better than the classical approach from these results (I will add more on this in the next points). Overall, I don’t think the contributions here are significant enough and the arguments don’t hold enough weight for me to accept this paper. 
3.	The whole ‘temporal continuity’ argument seems a little counterintuitive to me. The ‘time-aware’ loss function is designed to encourage the model to ignore differences at the time-scale of the time hyperparameter Tau, but you expect the model to maintain temporal differences at time-scales t > Tau. I think Tau needs to be much smaller than the time-scale of your expected changes for this to work. If you expect changes in cells to happen over a few hours, the hyperparameter Tau being 30 minutes doesn’t make sense – your model is just going to smooth out all temporal information. I know you are limited by the fact that you can’t take images, say, every 5 minutes, but the current setup doesn’t make sense to me.
4.	Just to add to the previous argument – in your current setup, it matters how long you train your model for, since overtraining could completely smooth out all temporal information. I don’t even know how you would design experiments to determine what a good number of epochs to train is without having an idea of how much temporal smoothness is ‘correct’. For example, in the limit of an infinite number of epochs under this loss function, all temporal information would be removed from your model. I just don’t see how you could both encourage temporal smoothness while maintaining a temporally faithful embedding when your data has a temporal resolution of 30 minutes over 24 hours.
5.	In the case of ‘time and cell-aware sampling’, how do you ensure that the model is robust to imaging factors like brightness or sensor noise? The point of such augmentations in the classical contrastive learning case is to teach the model to ignore spurious confounders which may actually show up in your real data – but the ‘time and cell-aware’ model never learns to do this. Is this model actually good at generalizing? What happens of your imaging conditions change a little? Would this model still work? I think many questions need to be answered here.
6.	I think the novelty proposed here lacks conceptual correctness in my view. With traditional ways of using temporal information in self-supervised learning, like predicting the temporal order of randomly flipped images, it makes sense how these would lead to a temporally unbiased and meaningful embedding space. My arguments in the points above highlight my concerns on why the proposed method may not be doing the same.
7.	Without actual ground truth annotations of fine-grained temporality, the only way to assess the quality of the embeddings is through the results on downstream temporal tasks. However, the classical contrastive sampling variant seems to perform better on the downstream infection classification task, which tells me that the classical method is leading to better quality embeddings than the proposed method.

### Questions
1.	I’m a little bit confused about the quantitative results. Specifically, you write “Therefore, we evaluate the accuracy of visual representation learned by our method using a biologically relevant benchmark: accuracy of the classification of the cell states with 3 hours of expert annotations. We compare our method with two baseline methods: fully supervised time-agnostic semantic segmentation of the infection state and time-agnostic contrastive learning. Compared to the ≈ 80% accuracy achieved by the supervised model and 60 − 65% accuracy achieved by the time-agnostic contrastive learning, DynaCLR models consistently achieve ≈ 95% accuracy.” I only see results in Table 1 that show classical contrastive sampling having an accuracy of 98.8%. Can you clarify where the results of the supervised model are and why there is a mismatch between the claimed values of 60-65% and the values shown in the table?
2.	When you say, “For the experiments in this paper, we set τ = 30 min, as we found this captures significant cell changes while maintaining temporal continuity without over-sampling.” Does this mean you tested with different τ values? If you did any experiments on this it would be good to include those, and would contribute to my concerns in the weaknesses section on temporal continuity and temporal faithfulness.
3.	In Section 3.3 you claim, “We compute (2) and (3) to evaluate the temporal evolution of the embeddings as a gradual, steady increase signifies strong temporal smoothness. In both figure 2 a) and 2 b), cell and time-aware sampling shows a smooth rising curve with minimal fluctuations. The classical contrastive method exhibits a rapid initial increase followed by plateaus, while the cell-aware approach shows intermittent fluctuations.” I’m not sure I see in Figure 2 what is described here. It seems like the curves for Euclidean distance are pretty similar between the different strategies. In fact, in the UMAP version it seems like the cell and time-aware version is most fluctuating (whether UMAP is an appropriate space in which to perform this is another question, since it is known to not maintain global structure). Can you please elaborate on this? I’m also unsure what you mean by “richness” of representation in Figure 2C and how you determined this.
4.	Can you elaborate the results of the integrated gradients based interpretability in Figure A1? What exactly is the model focusing on in the two channels? Can you provide evidence that this is relevant to the output task?
5.	You say “We observe a clear transition of cell states from interphase to mitosis as we follow the cells in UMAP space, particularly in models trained solely with the phase channel and incorporating temporal regularization” I kind of see what you’re trying to say but it’s still very unclear. Can you provide a mathematical comparison of the two models and show that one model is ‘smoother’ than the other over all cell division events?

### Soundness
2

### Presentation
3

### Contribution
2
