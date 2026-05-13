# Revisiting Long-term Time Series Forecasting: An Investigation on Affine Mapping

- Decision: Reject
- Scores: 5, 3, 6, 6

## Abstract
Long-term time series forecasting has gained significant attention in recent years. While there are various specialized designs for capturing temporal dependency, previous studies have demonstrated that a single linear layer can achieve competitive forecasting performance compared to other complex architectures. In this paper, we thoroughly investigate the intrinsic effectiveness of recent approaches and make three key observations: 1) linear mapping is critical to prior long-term time series forecasting efforts; 2) RevIN (reversible normalization) and CI (Channel Independent) play a vital role in improving overall forecasting performance; and 3) linear mapping can effectively capture periodic features in time series and has robustness for different periods across channels when increasing the input horizon. We provide theoretical and experimental explanations to support our findings and also discuss the limitations and future works.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Long-term time series forecasting (LTSF) is an important problem. Based on a finding from previous work that a linear layer can achieve forecasting performance comparable to complex models such as Transformers, in this paper, the authors study the effectiveness of recent approaches and provide various findings about their limitations. The authors provide theoretical and experimental explanations to support their findings.

### Strengths
1. This paper provides various types of visualization to support their claims and to present the results of experiments.
2. Simplicity is always appreciated. It is nice to observe simple models can achieve performance similar to or even better than complicated models.

### Weaknesses
1. The main claim of Section 2 is unclear. Are simple models always better than complex models for LTSF, or is it the case only to the specific framework shown in Figure 1? What if we adopt a different but still complicated framework, such as 1-dimensional CNNs with dilated convolutions or more complex architectures? How do the results change if we include traditional models such as AR (autoregression) or ARIMA, especially considering their known limitations with long-range dependencies, and how would this relate to the findings in this paper?
2. This paper is not self-contained. The experiments in Section 2 play a crucial role to motivate this work, but there is not enough description about the models and experimental setup. For example, RevIN is mentioned several times throughout the paper, but there is no definition of it. Furthermore, details regarding the specific hyperparameters used for each model, the optimization procedure, and the hardware used for the experiments are missing, making it difficult to reproduce the results. If the page limit is a problem, the authors could have added the details to Appendix.
3. Theorem 1 and 2, which are the main theoretical contributions of this work, seem trivial. If a time series can be clearly (and linearly) separated into seasonality and trend parts, I think it is obvious that a linear layer (or any linear function) is able to learn such separation. The theorems lack novelty and do not provide significant insights into the underlying mechanisms of LTSF. The assumptions made for the theorems, such as the clear separation of seasonality and trend, may not hold in real-world scenarios, limiting their practical applicability.

### Questions
1. What is the main improvement of this work from (Zeng et al., 2022)? This works seems like a re-verification of the claim made by the previous work.
2. What do the authors suggest as a result of this work? Should we replace the benchmarks for LTSF with simple linear models?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the recent approaches in Long-Term Time Series Forecasting (LTSF) especially around the one-pass prediction over a single linear layer that is seen to achieve competitive performance on par with other complex architectures.
The authors state that affine mapping in LTSF models effectively capture periodic patterns and thus dominates in the forecasting performance over the baseline models. However, there are no information about what affine mapping is or how affine mapping is effectively introduced in the LTSF models to improve performance.
The authors state that a single linear projection layer with Reversible Normalization (RevIN) outperforms the state-of-the-art models currently because the single layer feature extractor learns weights that are consistent with the projection layer which indeed imply a mapping pattern between input to output series. But this doesn’t effectively prove, affine mapping is the reason for the performance improvement.
The authors investigate the disentanglement of seasonal and trend terms of the time series model and state that there is research gap on the advanced models still left to explore. The authors also question the effectiveness of temporal feature extractors on LTSF tasks but there is no investigation around it that leads to the impact of the temporal feature extractors on the model performance other than affine mapping.
Finally, the authors run a series of experimental evaluation and state that the large models, PatchTST and TimesNet do not exhibit significant improvement over baseline single layer models and the authors are assuming it to be the models’ efficacy to learn periodicity through affine mapping. Also, in multiple channel use-cases, a single layer is observed to fail without modelling each channel independently which again questions the findings of the investigation.

### Strengths
1. The paper gives a detailed analysis of various use-cases of LTSF on public datasets and makes solid observations.
2. The authors prove the importance of Reversible Normalization(RevIN) and increasing input horizon on multi-channel on the LTSF model performances over multiple in-depth experiments.

### Weaknesses
1.  The findings of the paper in the abstract are not evidently proved in the experiments. Specifically, the claim that affine mapping dominates forecasting performance is not rigorously demonstrated. While the paper shows single-layer models perform well, it doesn't isolate the affine mapping component and prove it's the primary driver of performance. The experiments primarily focus on comparing single-layer models with and without RevIN, and with different input horizons, but they don't directly evaluate the contribution of the affine transformation itself, for example by comparing it to other types of mappings or by ablating it.
2.  This being an investigation paper, the experiments around affine mapping don’t include Mean
Bias Error for evaluation which effectively depicts the efficacy of affine transformation. The paper uses standard metrics like MSE and MAE, but these don't specifically highlight bias, which is crucial for understanding affine transformations. The lack of bias analysis makes it difficult to assess whether the affine mapping is truly capturing the underlying patterns or simply fitting the data with a systematic offset.
3.  The conclusion states that the affine mapping dominates in “some” LTSF models but there is no
detailed information on this generalized statement. The paper doesn't specify which models are dominated by affine mapping and under what conditions. This lack of specificity makes the claim difficult to interpret and apply to other contexts. The paper should provide a more precise characterization of the models and scenarios where affine mapping is most effective.
4. TYPOS: It’s a well-written paper. I had to point out just one on a high-level overview. Use of “Instead” and “Apart from” with “However” in the Introduction were slightly confusing. Please consider checking those.

### Questions
The work in this paper is detailed and had observations from extensive experiments on both simulated and real-world datasets, but the findings are inconsistent. The findings stated in the abstract are not derived across the experiments through the conclusion.
I believe there are many studies on why and how affine transformations can improve time-series forecasting models. As an investigation paper, I would recommend to consider the pros and cons of the current research to effectively conclude the findings and future work that is required on the topic. For example, in this paper, X. M. Chen, Y. Li, R. Z. Wang; Performance study of affine transformation and the advanced clear-sky model to improve intra-day solar forecasts. J. Renewable Sustainable Energy 1 July 2020; 12 (4): 043703., the results about affine transformation is similar to the findings of our paper. This paper should consider investigating the use-case used in this paper and fetch out the results and challenges faced in this use-case.

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors of this work study the long-term time series forecasting (LTSF) problem. They demonstrate that a single linear layer can perform competitively for LTSF compared to other complex architectures. Specifically, with theoretical analysis and empirical studies, the authors find that affine mapping is critical in LTSF tasks and inspect its efficacy. While dealing with multivariate time series data, the limitation of linear models is also discussed.

### Strengths
1. The authors study the fundamental mechanisms that affect the performance of recent LTSF models, which is important for the community. 
2. This work provides theoretical and empirical evidence to support its findings.
3. The presentation is well-organized and easy to follow.

### Weaknesses
1. As a research work submitted to a top-tier ML conference, the technical contribution is limited. In particular, novel solutions/algorithms that leverage the important findings are expected. 
2. It is better to investigate more real-world time series datasets with perplexing patterns.

### Questions
What about the efficacy of affine mapping when the models deal with noisy and low-quality time series data?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper offers a timely and rigorous critique of the recent trend of using transformer-based models for long-term time series forecasting, and arrives at several surprising and important empirical conclusions. One of these conclusions is that just a simple linear layer (as in DLinear) combined with RevIN (reversible instance normalization with a learnable affine mapping of statistics) results in superior long-term forecast performance. The second is, even more shockingly, that many popular transformer-based methods with random parameter initializations already outperform their trained counterparts on long-term multivariate point forecasting tasks. The paper further investigates failure modes of single-layer linear forecasters in the multivariate setting. 

The paper is well-written and of interest to the community in terms of the findings it offers. However, the novelty of the paper is limited for both methodology and theory.

### Strengths
The paper is well-written, and its empirical findings are surprising and insightful for time series forecasting practitioners. 

The first such conclusion results in a new and easy-to-implement model: RLinear. RLinear is simply DLinear with RevIN, and offers competitive performance. The second empirical exploration calls into question the use of large transformer architectures for forecasting. When using transformers to "extract features" the authors find that the learned mappings are easily confused and fail to capture the most basic signals with periodicity. In fact, this effect of "overfitting" appears so pronounced that the random initializations of these models appear to generalize almost better than their fitted counterparts. This is a very suprising finding that I look forward to verifying with the experimental setup the authors will make available.

The paper then moves to discussing why linear maps suffice to fit periodic signals. They offer an interesting comparative study of how linear models behave with different methods for normalization/disentanglement.

### Weaknesses
My main critique of the paper is its limited novelty. While the insights offered by the paper are quite useful, the main methodological advance offered simply combines two very recent ideas. Moreover, the validity of this method is also not rigorously tested with an ablation/comparative study. For example, there is no study as in Table 2 for the idea in Figure 8. Specifically, while Table 2 compares RLinear and RMLP against other complex models, it does not isolate the contribution of RevIN, or test the performance of RLinear with different normalization strategies, or evaluate alternative disentanglement techniques. This makes it difficult to ascertain the true source of performance gains. The theoretical results proposed in the paper are hardly novel. For example, Thm 1 barely needs to be denoted so (periodic functions can be reconstructed by shifting, and shifting is a linear operator..). Similarly, Thm 3 produces a somewhat unsurprising conclusion which is not contextualized well in the paper's presentation. The connection between the theoretical findings and the empirical results is not clearly established, making it hard to understand the practical implications of the theory. 

Among other points the authors may like to consider:
- For the uninitiated reader, the architecture of RLinear (and its simplicity) are hard to understand, and Figure 1 are hard to understand. Perhaps they could be revisited
- Footnote 4 and how it relates to the context is unclear.
- Please cite the DLinear paper with the accepted venue.
- Please revisit the conclusion section for grammar: e.g.,  "investigate" "where they generally prone" "encounter"
- Just a suggestion: The recent TiDE paper attacks some of the same problems as the authors. Although that work does not appear to be peer-reviewed yet it may be worthwihle to briefly discuss it in context.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
