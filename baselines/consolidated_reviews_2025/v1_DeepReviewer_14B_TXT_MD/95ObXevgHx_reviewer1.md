### Summary

The authors investigate the representation of language in 4 different brain regions during speech comprehension with ECoG. They fit encoding models to predict neural activity from GPT2-XL hidden states at different layers and investigate which layers are more predictive than others. They show that intermediate layers are most predictive of neural activity in all 4 regions and that the temporal response of neural activity best matches the representation of early layers early in time and late layers later in time.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The authors present an interesting investigation of the representation of language in the brain by fitting encoding models to neural data recorded during natural speech comprehension. They show that the neural representation of language unfolds over time in a way that is similar to the representations of layers in GPT2.

### Weaknesses

#### Some Related Works


#### comment

The authors claim that their results provide evidence that representations in the brain are similar to the hierarchical representations in GPT2. I do not think this claim is supported by their results. The fact that intermediate layers are more predictive of neural responses does not mean that the brain is representing language in a hierarchical way. The authors should rephrase their claims to make it clear that they are only showing that neural representations are similar to GPT2 representations, not that neural representations are hierarchical.

The authors should more clearly explain why their results demonstrate that the brain represents language in a hierarchical way. The fact that intermediate layers are more predictive of neural responses does not necessarily mean that the brain is representing language in a hierarchical way. It could be that intermediate layers are simply the best linear combination of all layers, or that they capture some other property of the data that is not related to hierarchical processing. The authors need to provide more evidence to support their claim that the brain is representing language in a hierarchical way.

The authors should also clarify what they mean by “hierarchical”. Do they mean that early layers represent lower-level features and later layers represent higher-level features? If so, what are the lower-level and higher-level features in the context of language processing? Are they referring to phonemes, words, phrases, or sentences? A more precise definition of “hierarchical” is needed.

The authors should also clarify the distinction between encoding and decoding. In their paper, they use encoding models to predict neural activity from GPT2 hidden states. However, they sometimes refer to their results as if they were using a decoding model to infer neural activity from GPT2 hidden states. This is confusing and should be clarified.

The authors should also clarify the distinction between “brain activity” and “neural activity”. In their paper, they use these terms interchangeably. However, “brain activity” could refer to a wide range of different signals, such as EEG, MEG, or fMRI, while “neural activity” specifically refers to the activity of neurons. The authors should be more precise in their terminology.

The authors should also clarify the distinction between “brain activities” and “neural activities”. In their paper, they use “brain activities” to refer to the neural activity in different brain regions. However, this is an awkward phrasing and should be avoided. The authors should use “neural activity” instead.

### Suggestions

The authors should provide a more detailed analysis of the relationship between the different layers of GPT2 and the neural activity in different brain regions. For example, they could investigate whether the representations in early layers are more similar to the representations in early auditory cortex, while the representations in late layers are more similar to the representations in higher-level language areas. This would provide more evidence for the claim that the brain is representing language in a hierarchical way. They could also investigate whether the representations in different layers are linearly separable, which would provide more evidence for the claim that the different layers are capturing different aspects of the data.

The authors should also investigate whether the hierarchical representations in GPT2 are necessary for predicting neural activity. For example, they could compare the performance of their model to a model that uses only a single layer of GPT2, or a model that uses a random combination of layers. If the hierarchical structure of GPT2 is important for predicting neural activity, then these models should perform worse than their model. This would provide more evidence for the claim that the brain is representing language in a hierarchical way. They could also investigate whether the hierarchical representations in GPT2 are specific to language processing, or whether they are a general property of the model. This could be done by comparing the representations in different layers for language and non-language tasks.

Finally, the authors should be more precise in their terminology and avoid using ambiguous terms such as “brain activity” and “decoding”. They should also avoid using awkward phrasing such as “brain activities”. They should also provide a more precise definition of “hierarchical” and explain what they mean by this term in the context of language processing. By addressing these issues, the authors can make their paper more clear and convincing.

### Questions

The authors should clarify the distinction between encoding and decoding. In their paper, they use encoding models to predict neural activity from GPT2 hidden states. However, they sometimes refer to their results as if they were using a decoding model to infer neural activity from GPT2 hidden states. This is confusing and should be clarified.

The authors should clarify the distinction between “brain activity” and “neural activity”. In their paper, they use these terms interchangeably. However, “brain activity” could refer to a wide range of different signals, such as EEG, MEG, or fMRI, while “neural activity” specifically refers to the activity of neurons. The authors should be more precise in their terminology.

The authors should clarify the distinction between “brain activities” and “neural activities”. In their paper, they use “brain activities” to refer to the neural activity in different brain regions. However, this is an awkward phrasing and should be avoided. The authors should use “neural activity” instead.

### Rating

3: reject, not good enough

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
