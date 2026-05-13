# IRGen: Generative Modeling for Image Retrieval

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
While generative modeling has become prevalent across numerous research fields, its integration into the realm of image retrieval remains largely unexplored and underjustified. In this paper, we present a novel methodology, reframing image retrieval as a variant of generative modeling and employing a sequence-to-sequence model. This approach is harmoniously aligned with the current trend towards unification in research, presenting a cohesive framework that allows for end-to-end differentiable searching. This, in turn, facilitates superior performance via direct optimization techniques. The development of our model, dubbed IRGen, addresses the critical technical challenge of converting an image into a concise sequence of semantic units, which is pivotal for enabling efficient and effective search. Extensive experiments demonstrate that our model achieves state-of-the-art performance  on three widely-used image retrieval benchmarks as well as two million-scale datasets, yielding significant improvement compared to prior competitive retrieval methods. In addition, the notable surge in precision scores facilitated by generative modeling presents the potential to bypass the reranking phase, which is traditionally indispensable in practical retrieval workflows.

  \keywords{Image Retrieval \and Autoregressive Model \and Generative Model}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes an approach which learns the encoding and indexing structure jointly for improving improving image retrieval task. It relies on VIT backend for encoding and Residual Quantization (RQ) for hierarchical semantic representation learning. The proposed solution is optimized end-to-end unlike traditional approach of creating content embeddings and running approximate nearest neighbor (ANN) search independently. The solution is evaluated across multiple dataset and multiple baseline embedding models (fine-tuned on the same dataset) coupled with different ANN search algorithms. The results indicate significantly improved the image retrieval results.

### Strengths
- Provides a simple, intuitive and technically sound approach, which borrows strong insights from the recent generative modeling literature and Residual Quantization concepts. 
- There are multiple baselines and numerous ablations to provided for evaluations. Outperforms strong baselines. 
- The paper is well motivated and written.

### Weaknesses
 - The concept of joint training the embedding model and index structure is not entirely novel 
- The approach scales well for million scale datasets, but not billions

- Figure 4: The precision of the proposed approach increases as top-k increases. The expectation is that there should be a trade-off. 
- Table 4: The generalization capability of the approach is demonstrated by taking out 5% of the ImageNet dataset during training and used them for inference/testing. However, those 5% examples are coming from the same ImageNet dataset distribution. The model already learned the semantic classes and their visual variations. Therefore this experiment does not fully demonstrate the out-of-domain capability of the proposed method. Also, it is not clear if the same treatment applied for the other baseline model compared. Need more clarity and justification for this experiment. 
- There is a need for a table comparing the capacity and inference cost of the baseline models to the proposed solution in the Appendix (for Apples-to-Apples comparisons). A similar comparison is also needed for the retrieval stage. At million scale, even linear search is quite practical. It would be also great to have ablations where the model capacity is varied and the overall performance is evaluated. 
- Residual Vector Quantization also uses beam search and RVQ codes may be used for efficiently knn search using prefix trees (or better with Aggregating Tree). Therefore the inference time operations are quite similar to IRGen paper except that the previous paper does not train an encoding for the search task. This could also serve as a natural baseline which would demonstrate the need for joint training of encoder and indexing/search structures. OR, after training the encoder, but could we combine and use the below paper for a more scalable (billions) search? A discussion should suffice.
Liu et al, "Generalized Residual Vector Quantization and Aggregating Tree for Large Scale Search", IEEE T on Multimedia, 2017
- Sanity check: Are the reported results for IRGen the-state-of-the-art today for the target image retrieval benchmarks? This should be stated clearly in the paper. If not, we need comparison with the SOTA method.

### Questions
- The concept of jointly training the retrieval / embedding model and ANN index structures (or search models) is not novel. It would be great to have a more in depth review of these approaches. A quick example: "Joint Learning of Deep Retrieval Model and Product Quantization based Embedding Index", SIGIR'21. https://dl.acm.org/doi/10.1145/3404835.3462988 
- Figure 4: The precision of the proposed approach increases as top-k increases. The expectation is that there should be a trade-off. 
- Table 4: The generalization capability of the approach is demonstrated by taking out 5% of the ImageNet dataset during training and used them for inference/testing. However, those 5% examples are coming from the same ImageNet dataset distribution. The model already learned the semantic classes and their visual variations. Therefore this experiment does not fully demonstrate the out-of-domain capability of the proposed method. Also, it is not clear if the same treatment applied for the other baseline model compared. Need more clarity and justification for this experiment. 
- There is a need for a table comparing the capacity and inference cost of the baseline models to the proposed solution in the Appendix (for Apples-to-Apples comparisons). A similar comparison is also needed for the retrieval stage. At million scale, even linear search is quite practical. It would be also great to have ablations where the model capacity is varied and the overall performance is evaluated. 
- Residual Vector Quantization also uses beam search and RVQ codes may be used for efficiently knn search using prefix trees (or better with Aggregating Tree). Therefore the inference time operations are quite similar to IRGen paper except that the previous paper does not train an encoding for the search task. This could also serve as a natural baseline which would demonstrate the need for joint training of encoder and indexing/search structures. OR, after training the encoder, but could we combine and use the below paper for a more scalable (billions) search? A discussion should suffice. 
Liu et al, "Generalized Residual Vector Quantization and Aggregating Tree for Large Scale Search", IEEE T on Multimedia, 2017
- Sanity check: Are the reported results for IRGen the-state-of-the-art today for the target image retrieval benchmarks? This should be stated clearly in the paper. If not, we need comparison with the SOTA method.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel approach for image retrieval using generative modeling -- IRGen. IRGen is a sequence-to-sequence model that, given a provided query image, directly generates "identifiers" corresponding to the query’s nearest neighbors. Specifically, the model takes a query image as input and autoregressively predicts discrete visual tokens, which are considered as the identifier of an image. These discrete visual tokens are learned through classification loss, the global features of an image is tokenized through residual quantization. Once the semantic image tokenizer is trained, then a decoder is learned to predict the identifier of query's nearest neighbor through autoregressive way. In summary, this paper propose a novel approach to tokenize an image into semantic identifiers and achieves state-of-the-art over conventional methods.

### Strengths
originality:  the paper proposes a novel approach for image retrieval using generative modeling. The semantic image tokenizer with residual quantization is elegant and the generative modeling way is quite interesting. The whole framework looks pretty straightforward and simple.

quality: the paper is technically sound. Extensive experiments were performed.

clarity: the paper is well-written and well-organized.

significance: the paper address image retrieval with generative modeling which is quite an interesting way, showing the possibility of using generative method to obtain codes for retrieval. Hence this paper can inspire many future works, such as how to learn a code that can do both generation and retrieval, how to speed up the search (e.g., with hash codes/without beam search).

### Weaknesses
 - the description of how the beam search is a little bit confusing to me. I couldn't fully understand how it is done.
- retrieval with autoregressive means the retrieval may not enjoy the benefit of maximum inner-product search
- as the current retrieval is done with GPU, if using CPU, the decoder process will be significantly slowed down and may affect the retrieval speed

### Questions
1. does the semantic tokenizer share the weights with the encoder? 
2. seems like we can directly use the code from semantic tokenizer for image retrieval -- similar to how product quantization performs retrieval, what is the necessity of employing the decoder? What is the disadvantange/how much performance degrades if we just use the semantic tokenizer's code for retrieval?
3. what is the retrieval speed of using IRGen on CPU compared to IVFPQ/ScaNN/SPANN?
4. what if you train a normal classification model, then perform PQ to obtain the "tokens" instead of the proposed semantic tokenizer?
5. is a two-stage training process? can they be trained end-to-end?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces an image retrieval method built upon semantic image tokenization. Recognizing the limitations of popular tokenization techniques like VQ-VAE and RQ-VAE for retrieval tasks, the authors propose a more efficient approach that emphasizes global feature extraction from class tokens, reducing sequence lengths and emphasizing high-level semantic information. To enhance semantic representation, they also incorporate classification loss training. In tandem, an autoregressive encoder-decoder architecture is employed that decouples input embedding from discrete code generation, focusing on understanding semantic relationships between image pairs. During the inference stage, beam search is used to efficiently find top-K matches for a given query image. The model's end-to-end design ensures efficient retrieval and offers a novel perspective compared to traditional approximate nearest neighbor search techniques.

### Strengths
1. The paper introduces an encoder-decoder architecture that decouples input embedding from discrete code generation. This design, focusing on understanding the semantic relationships between image pairs, offers a more flexible and adaptable framework, potentially making the model more robust and applicable across various datasets and retrieval scenarios.

2. The model's design places a significant emphasis on capturing high-level semantic information. By incorporating classification loss training on both original and reconstructed embeddings, the proposed approach ensures that the retrieved images are semantically relevant to the query, bridging the gap between low-level details and meaningful content.

3. The paper acknowledges the inefficiencies of traditional tokenization techniques for image retrieval and introduces an approach that reduces sequence lengths. By focusing on global feature extraction from class tokens, the model offers a more streamlined and efficient representation, especially suited for retrieval tasks.

### Weaknesses
1. While emphasizing global feature extraction from class tokens might improve efficiency, there's a risk of overlooking crucial spatial information present in other parts of the image, possibly leading to incomplete or less accurate retrieval results. The reliance on class tokens as the sole source of image representation could be particularly problematic for images where fine-grained details or spatial arrangements are critical for distinguishing between similar instances. For example, in a dataset of bird species, subtle differences in feather patterns or beak shapes might be missed if the model only focuses on high-level class-related features.

2. The paper proposes the use of beam search for efficient top-K retrieval, but this method can be computationally intensive, especially for large image databases. Additionally, validating each generated image identifier can be a time-consuming process, even with their proposed prefix tree optimization. The computational cost of beam search grows exponentially with the beam width and sequence length, making it potentially unsuitable for very large-scale retrieval tasks. The paper does not clearly specify the complexity of the prefix tree search and how it scales with the size of the image database.

3. The approach, especially the beam search with constraints, may face scalability issues when dealing with vast and diverse image datasets. As databases grow, the efficiency and accuracy of the method may be challenged. The paper lacks a detailed analysis of how the proposed method performs with varying database sizes and complexities. It is unclear whether the method can maintain its performance when the number of images increases by orders of magnitude.

4. While the method aims to capture high-level semantics, it might not generalize well across diverse datasets with varying characteristics. The paper does not address how the model would adapt to datasets with vastly different semantic structures or image content. For instance, a model trained on natural images might not perform well on medical images or satellite imagery without significant retraining or adaptation. The paper should discuss the limitations of the model in terms of domain generalization.

5. There seems to be a limited discussion on how this method performs compared to other state-of-the-art techniques. Without comprehensive comparative studies, it's challenging to ascertain the model's effectiveness and superiority in real-world scenarios. The paper should include a more thorough comparison with other retrieval methods, including both embedding-based and generative approaches, on a wider range of datasets.

### Questions
1. How do you ensure that the emphasis on global feature extraction from class tokens doesn't compromise the finer spatial details of the image, which could be vital for certain retrieval scenarios?

2. Given the complexities of beam search, especially for large image databases, what specific optimizations have you implemented to ensure real-time or near-real-time retrieval performances?

3. How does the proposed model handle noisy or imperfect image datasets? Are there specific preprocessing steps or augmentations recommended to enhance retrieval accuracy?

4. How adaptable is the autoregressive encoder-decoder architecture to other types of multimedia content, such as videos or audio? Are there potential modifications or extensions to the proposed method for such content?

5. Given the model's dependency on class tokens, how does it handle images that may not fit neatly into predefined classes or those that belong to multiple overlapping classes?

6. You have mentioned using classification loss for training. Were other loss functions explored during the development? If so, how did they impact the model's performance?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper poses image retrieval as a form of generative modelling in order to allow the use of common transformer architectures for search in an end-to-end fashion. The proposed IRGen gets a query image as input and outputs identifiers that correspond to the nearest neighbors of the query in a given image database. This effectively turns search into a problem solved by a large transformer encoder-decoder
combines the two classical steps of image retrieval (feature extraction and indexing/search) into one module, that has to be trained for a given database.

They introduce a "semantic image tokenizer" that transforms an image into a sequence of tokens by only taking into account a global image feature from the CLS token. They use resdual quantization and alternative optimization to

### Strengths
The paper deals with an interesting formulation of image indexing as a sequence problem over quantized representations.  A differentiable index is used and therefore one can finetune the model end to end. Despite there are a number of unclear parts regarding the papers actual contribution and evaluation protocol, the fact that this approach works well is interesting.

### Weaknesses
1) The paper is written in a way that is hard to follow and understand, both the method and the contributions. Figure 1 is ambiguous or wrong.

2) A lot of relevant work is missing and therefore so is proper discussion on the method's relation to other works, especially in the area of deep quantization and hashing. Some example are listed below, many more can be found through the works listed.

3) The paper's contributions are unclear and while there are 2 components introduced, they are only tested together and it is hard to understand the contribution of each. Specifically, The tokenizer is pretrained on top of a large visual encoder (ViT from CLIP) independently from the index via alternative optimization. This module gives a set of codes that can be used for retrieval. The performance of those codes (seen as quantization codes) is not evaluated, while a clear discussion on technical differences and contributions to other residual quantization methods or other recent works on deep quantization or hashing is missing. It is also unclear how much the fact the quantized codes are a sequence matters, versus eg using simple PQ codes that have a much easier to optimize objective. Note that the method here uses annotated data from the downstream task, therefore the fair comparisson would be vs supervised quantization methods. 

4) The large AR model on top acts as a differentiable index. There is no proper discussion on how this compares to other differentiable indexes from a technical perspective. The only difference mentioned to other recent differentiable indexing methods in the end of sec 4 is that the input features (document identifiers) are obtained in a different way, but this has nothing to do with the actual differentiable index modeling part. 

5) The training objective is not much different from pairwise objectives on top of quantized codes used in quantization/hashing works. Although one has to pass through the index, only image pair codes are used for computing the loss. This is why beam search is needed at test time,  ie there is a clear train test discrepancy here, same as training deep hashing. I cannot see how this is more "end2end", as the objective of the loss is not a full database ranking objective. Also note that beam search is a complex data structure that keeps multiple paths and also "a prefix tree containing valid codes". One can say maybe that beam search is in itself as complex as any other indexing structure.

6) Experimental validation is generally lacking. As mentioned above, the contrubution of the two modules separately shoudl be studied. Also, reporting the precision and recall metrics in isolation is not the best for image retrieval. Results with mAP (or at least mAP100) for all datasets should be presented. Also results on classic retrieval datasets like Oxford and PAris [ir1] are missing. 

7) inference speed experiments lacking and misleading: The proposed method has a large computational overhead, ie a large transformer decoder instead of a simple index. Basically, a comparisson versus FT-CLIP + some indexing is needed, but I can only see the proposed approach to be possibly even orders of magintude slower: excluding feature extraction with CLIP (the proposed method uses CLIP as the encoder to give to the tokenizer), the proposed method needs at test timeto also 1) to tokenize, 2) pass through a large ViT decoder  (12
transformer decoder block with dimension 768 for the small datasets, 24 layers for IamgeNet) and 3) beam search. Instead, Ft-CLIP with a basic IVFPQ index only needs to search the index and this is really really fast.

8) The model is highly task specific: a different trained AR model/index is needed for every database. Also it is unclear how such an index can handle changes in the database

### Questions
Please respond to the comments above.

Q1: In Fig 1 shouldnt the tokenizer get the ouput of a visual encoder as input? ie f_cls? where is that? Is "Semantic Image Tokenizer" a separate encoder than the "transformer encoder" in Fig 1? 
Q2: For the same image encoder f_cls, what is the retrieval performance of the proposed tokenizer vs other PQ/hashing tokenizers?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
