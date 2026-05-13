# Advancing Energy Efficiency in On-Device Streaming Speech Recognition

- Decision: Reject
- Scores: 6, 3, 3

## Abstract
Power consumption plays a crucial role in on-device streaming speech recognition, significantly influencing the user experience. This study explores how the configuration of weight parameters in speech recognition models affects their overall energy efficiency. We found that the influence of these parameters on power consumption varies depending on factors such as invocation frequency and memory allocation. Leveraging these insights, we propose design principles that enhance on-device speech recognition models by reducing power consumption with minimal impact on accuracy. Our approach, which adjusts model components based on their specific energy sensitivities, achieves up to 47% lower energy usage while preserving comparable model accuracy and improving real-time performance compared to leading methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study conducted extensive experiments to analyze power usage in ASR models, examining its correlation with model runtime behaviors and identifying strategies for power reduction. The findings are:
1) The majority of ASR power consumption is attributed to loading model weights from off-chip memory, intricately linked to the size of model components, their invocation frequency, and their memory placement. 
2) Despite its smaller size, the Joiner component consumes more power than the Encoder and Predictor, due to these factors. 
3) A notable exponential relationship between the model’s word error rate and the encoder size. 

Utilizing these insights, a series of design guidelines focused on model compression for enhancing energy efficiency is formulated. The application of these guidelines on the LibriSpeech and Public Video datasets resulted in significant energy savings of up to 47% and a reduction in RTF by up to 29%, all while preserving model accuracy compared to the state-of-the-art methods.

### Strengths
The paper is generally well-written and clear. 
Experiments are extensive and logically organized.
The findings and the design guidelines are new and would be interesting to the community.

### Weaknesses
The investigation taken in this paper is mainly empirical, using well-known techniques, with minor contributions in models and methods. The paper reads more like a good industry technical report, with extensive empirical experiments. The core methodology relies on profiling power consumption of different ASR model components, which is a standard practice. While the analysis of the Joiner component's power usage is interesting, the paper lacks novelty in its approach. The compression techniques applied are also relatively standard, such as pruning and quantization, and the paper does not introduce any novel compression algorithms or optimization strategies. The reported energy savings, although significant, are achieved through well-established methods, making the overall contribution incremental rather than groundbreaking.

### Questions
see above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the problem of minimizing power consumption for on-device ASR utilizing the neural transducer architecture.  It is first shown that the bulk of power consumption is not in computations but instead in memory access for various modules of the ASR model.  Based on previously known power consumption benchmarks for accessing various memory types, a model of relationship between size and frequency of use of modules to their power consumption is identified.  Further, using empirical data, a relationship between module size and ASR word error rate (WER) is established.  Using these relationships, an iterative procedure is proposed that identifies, at every step, the module to compress that’ll lead to the largest drop in power consumption for the least impact on WER, until the target power savings are achieved.

### Strengths
* A systematic approach to optimizing energy efficiency of models for on-device ASR.
* Overall well written paper (except a key lack of clarity as pointed out below).

### Weaknesses
 * Lack of clarity around power consumption data in experiments.  The power consumption results presented in Figures 6 & 7 are labeled ‘Model Power Consumption’ — are these model based estimates, or real measurements of power consumption?  If these are model based estimates then what indication is there to suggest these will correlate with real measurements?  Specifically, the paper does not detail the specific hardware platform used for the experiments, nor does it describe the methodology for how the power consumption was measured or estimated.  Without this information, it is difficult to assess the validity of the power consumption results. For example, if the power consumption is estimated using a model, what are the parameters of the model, and how were these parameters obtained?  Furthermore, how does this model account for variations in power consumption due to different memory access patterns or CPU utilization?
* The WER vs model size graphs seem slightly worse for the proposed approach as compared to baseline in Figures 6 & 7.  This is understandable as the focus was not on optimizing for model memory as a function of WER.  However, would the proposed approach be effective if the focus was on minimizing model memory footprint?  It is unclear if the proposed iterative compression approach could be adapted to directly minimize model size, or if it is fundamentally limited to power consumption optimization.  The paper does not discuss the potential trade-offs between power consumption and model size, and whether a multi-objective optimization approach could be beneficial.

### Questions
Please see 'weaknesses' section above

### Soundness
2

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
5

### Summary
This paper studies the energy efficiency of speech recognition models on the Pixel 5. It varies the model size via Adam-pruning to reach sparse variants of some unspecified base model and then looks at WER, RTF and power consumption, on Librispeech and some in-house Public Video dataset.

### Strengths
- Power consumption is very relevant to study.

- A lot of different model sizes have been tested.

### Weaknesses
 - This uses a Pixel 5 without any neural hardware acceleration. Most modern mobile devices have some neural accelerator chip, and such a study on power consumption should use it. This will heavily influence all the results presented in the paper here. The presented results are not really so relevant nowadays that we have such neural accelerators.

- Adam-pruning to introduce sparsity to make the model smaller is the only method used here to vary the model size. There are many other ways to vary the model size, even more straightforward, to just change the number of layers and/or number of dimensions (then train from scratch or via knowledge distillation from a big model). When I see different model sizes, I think this is much more expected and relevant. But you can also compare different methods (Adam-pruning vs just changing num layers/dims vs maybe some other methods). But such comparison is not done here.

- Sparsity is probably a suboptimal choice for neural accelerator chips. So this is even more an argument for using other methods to vary the model size.

- The base model is not specified at all.

- There is no code.

- The relevant properties are WER, RTF and power consumption, and you would want to see them being put directly into relation to each other. This is not done here. It's always only indirect via model size.

- Comparison of different encoders (Emformer vs Conformer vs maybe others, e.g. Zipformer) is missing.



### Questions
Table 1: Expand on "typical model": What kind? Transducer? What encoder? Conformer? What WERs does it get? What search (beam search or greedy)? Used together with LM or standalone? If with LM, what kind of LM? Also, better specify the model size in terms of num layers and num dimensions, not in number of absolute parameters (or maybe both).

(Fig4) I guess "compressing" means that you do Adam-pruning? It would be helpful to add that to the figure caption. I was confused initially about what it means.

So, for all the different model sizes throughout the whole paper, it's always Adam-pruning from some base model? What is actually the base model? Maybe I overlooked it, but I never really saw that specified. How many layers? How many dimensions? You use Emformer for Librispeech and Conformer for Public Video. Why not compare Emformer and Conformer for Librispeech? Why to select a different encoder in each case? That makes it not really consistent now. And what is the configuration of the decoder? It's an LSTM? How many layers? What dimensions? And same question for the joiner network.

(Sec 5.2) "the choice and performance of the baseline are not critical in this context." - why? I think they are. Please specify them.

What happens when you train models of different sizes from scratch? Or via knowledge distillation from a big model? You can also change number of layers, number of dimensions, which is maybe better than the Adam-pruning? E.g. when searching for the best configuration for some given power budget, maybe that way you can find better models? Now you are restricting yourself to just one very specific kind of varying the model size.

To expand, now you are restricting yourself to introduce sparsity (via Adam-pruning). How does this compare to changing the number of layers and/or number of dimensions, in terms of power consumption and WER?

(Sec 3.2) "This exponential relationship suggests diminishing returns with increasing encoder size" - again, if I understand correctly, this is always for a given base model, always with fixed num layers / num dims, just making it more sparse? So then this statement is wrong. You cannot make this statement. I am not sure if the relationship is really exponential when you change the model size via other means (e.g. num layers / num dims).

Fig 4c, very noisy. This is maybe due to Adam-pruning. It would maybe help to train different base models with different random seeds, then apply the Adam-pruning, and then do the average of the results.

You plot either WER to model size, or Power consumption to model size, or RTF to model size. But I think much more interesting would be to combine that, and then have e.g. WER to Power consumption, or RTF (given some fixed WER) to power consumption, or RTF (given some fixed power consumption) to WER, or similar. The model size is never really relevant. The three other metrics (WER, RTF, power consumption) are relevant, and you want to know what the relation between those are.

What accelerator hardware is used? You say, you use a Google Pixel-5. Does it use the GPU?

I think the choice of Pixel 5 is a bit weird. Most modern phones have some sort of neural accelerator chip (Google Tensor G4, Apple Neural Engine), and you would want to use them, as they are optimized to do such computations, also in terms of power efficiency. And the Pixel 5 does not, as far as I know (or only maybe the GPU?). This questions the whole relevance of the presented study here. Also because sparsity is maybe not so optimal of such a chip, but instead you would change num layers or num dimensions, or maybe other aspects of the model.

(Sec 1) "we discovered that the energy consumption of individual ASR model components is influenced not only by their respective model sizes but also by the frequency with which they are invoked and their memory placement strategies." - I don't really see that you show this in the paper.

### Soundness
1

### Presentation
2

### Contribution
1
