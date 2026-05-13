# Plausibly Deniable Encryption with Large Language Models

- Decision: Reject
- Scores: 3, 5, 3, 5, 8

## Abstract
We present a novel approach for achieving plausible deniability in cryptography by harnessing the power of large language models (LLMs) in conjunction with conventional encryption algorithms. Leveraging the inherent statistical properties of LLMs, we design an encryption scheme that allows the same ciphertext to be decrypted with any key, while still yielding a plausible message. Unlike established methods, our approach neither relies on a fixed set of decoy keys or messages nor introduces redundancy. Our method is founded on the observation that language models can be used as encoders to compress a low-entropy signal (such as natural language) into a stream indistinguishable from noise, and similarly, that sampling from the model is equivalent to decoding a stream of noise. When such a stream is encrypted and subsequently decrypted with an incorrect key, it will lead to a sampling behavior and will thus generate a plausible message. Through a series of experiments, we substantiate the resilience of our approach against various statistical detection techniques. Finally, although we mainly focus on language models, we establish the applicability of our approach to a broader set of generative models and domains, including images and audio.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper investigates the possibility of using a large langage models (LLMs) to provide plausible deniability for conventional encryption schemes in which the objective is to provide a user with the possibility of opening a particular ciphertext under a different key. More precisely, the objective is first to use the LLM to produce a low-level representation of the plaintext before encrypting it using a classical encryption scheme such as AES.

### Strengths
-The idea of using a large language model to provide plausible deniability is highly original and provides an interesting example of the combination of recent advances in machine learning with cryptography. More precisely, using the compression capability of LLMs seem interesting approach to be able to achieve plausible deniability. 
-The paper is well-written and the authors have done a good job at introducing the necessary background on encoding and decoding. 
-Beyond the use of LLMs, the proposed approach is also tested on ImageGPT, which demonstrates the wide applicability of the proposed approach.

### Weaknesses
-A detailed characterization on whether the encoding/decoding part can possibly cause a difference on the plaintext in the « normal » situation in which the encryption is performed normally is currently missing from the paper. For instance, what happens if the value of k is less than 32, does it mean that the decoding will result in a different message with a high probability? This is particularly concerning as the paper does not specify the minimal value of k for which the encoding/decoding process is lossless, and how this value impacts the security of the scheme. The lack of a formal analysis on the impact of k on the correctness of the decoding process is a significant issue.
-The security analysis should also be more detailed. For instance, it is not clear what are « the optimality assumptions » mentioned in the paper that makes the ciphertext indistinguishable from white noise. Overall, the paper lacks a detailed proof of the security of the proposed scheme. In addition, it also lacks as a review of the main existing families of definitions of the concept of plausible deniability and a detailed discussion on how the proposed notion compares to this. The paper should include a formal definition of the security notion it aims to achieve, and demonstrate that the proposed scheme satisfies this definition under clearly stated assumptions. The current analysis is insufficient to claim any meaningful level of security.
-The transmission of prompting as as external unencrypted information alongside the ciphertext seems to defeat the purpose of plausible deniability as it will directly indicate to the adversary that there is a tentative to generate a message providing plausible deniability. This is a critical flaw, as the prompt itself reveals the intention of using a deniable encryption scheme, thereby undermining the deniability aspect. The paper needs to address this issue by either removing the prompt or providing a method to transmit it securely.
-The frequency and correlation tests that are proposed to evaluate the random aspect of the encoded string may not be sufficient to provide a level of security that is required in a cryptographic setting. If possible the authors should clarify whether such test are sufficient to assess the quality and security of cryptographic random number generators. These tests are not sufficient to guarantee the unpredictability of the encoded string, which is a crucial requirement for cryptographic security. The paper should consider more robust statistical tests and provide a theoretical analysis of the randomness of the encoded string.
-It seems that even when the decoding is performed with a different key that a lot of the semantics is preserved (for instance an address is still decoded towards an address). This seems to result in the possibility for an adversary to infer some significant information about the cleartext, which is in contrast to other proposal for deniable encryption. This might be due the information contains in the prompt, which significantly contraints the possible decryption but still this leads to a non-trivial leakage.

### Questions
-What does a consensus on a model means in practice (introduction)?
-See also the main issues raised in the weaknesses section.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper shows how to use (generative) language models to compress and decompress natural sentences, in a way that the encoded (compressed) strings are almost fully using the entropy bound. Hence, a random junk codeword can also be decoded into a random looking sentence.

The idea is to deterministically encode each token $T_i$ with a number $t_i$ in such a way that $t_i$ would allow us to pick $T_i$ again if we had recovered the previous tokens already based on the CDF of the $i$th token's distribution. 

The paper then relies on this idea to give an application to "deniable encryption" as follows. We encrypt a message m but first compressing it into a string of numbers $t_1,...$ and then encrypting these strings using standard encryption. Now, if we use a fake key, we end up with a random sequence $s_1,s_2,\dots$ instead, which will lead to another generated (natural looking) sentence.

The paper then discusses some extensions, e.g., to use prompts to contextualize the message. For example if the message is a date, the prompt starts with something that guides the generated message to be a date.

Finally, the paper does some statistical tests to see how indistinguishable are the original texts from the fake decoded variants, and concludes that hey are closely distribution but not fully the same.

### Strengths
The strength is to find a nice application to the deniable encryption setting, using the "compressing/decompressing" capability of LLMs.

### Weaknesses
The paper's main application is a crypto application. This means the paper needs to be much more formal about its claims, yet the paper does not even have a formal definition of deniable encryption.

In my view, the core contribution of the paper is to derive compression/decompression techniques based on LLMs.
Yet, there seems to be older works on using LLMs for compressing language to its core entropy (eg., this work  from two years ago:
https://www.semanticscholar.org/paper/Lossless-text-compression-using-GPT-2-language-and-Rahman-Hamada/cde63fb5a385fc209107944c6fe19b2d618c407c

Also, since the authors agree that compression using LLM has been done before, then why is not it that any compression scheme (that encodes natural sentences to close-to their optimal entropy bound) can be used? Just take a string s, encode it into string t, and encrypt t using a one-time pad type encryption (that XORs an inflated key with the message). Then, any perturbed key will decrypt the ciphertext to another string t' that can be decoded to another natural sentence. If you agree that compression is not your novelty, it seems the whole paper's idea is what I wrote in this paragraph, no? Please let me know if I am missing something.

Also, I add that if the main application here is an encryption algorithm, it is much better to be submitted to a cryptography venue to get the proper scrutiny that is highly needed for a new encryption scheme.

### Questions
Do you know need any formal properties from the underlying crypto encryption scheme? You say you use AES but I wonder what is needed at abstract level. It seems the scheme itself should have some form of deniability built in so that a random key allows decryption into a legitimate-looking string.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes the use of LLMs as an encoder/decoder to add a layer of plausible message deniability on top of ordinary encryption. The idea is to make use of the entropy of an incorrect key choice to provide the randomness needed for sampling from the LLM to generate plausible messages without expanding the ciphertext that must be transmitted. It presents experimental results show that incorrect keys do in fact sample to plausible messages.

### Strengths
The core idea of this paper is very interesting: LLMs might provide plausible alternative messages given the entropy of an other-than-intended key in a way that reduces the need to send message alternatives or cover traffic or otherwise steganographically encode alternatives in the real message. Presumably, the LLM could be treated as a kind of "shared setup" parameter in the usual cryptographic formalism, and even large values of this kind are regularly considered as part of the cryptography literature. The experimental results showing the positive relationships between sampling strategies for various models are also suggestive that this strategy can be made to work. And some of the ideas about how to build sampling strategies and deal with, e.g., quantizing the distributions that must be sampled from seem useful and helpful.

### Weaknesses
I would expect a paper on a cryptography topic - or really any topic in information security - to provide a concrete threat model or security model. In the cryptography literature, these are generally formal and mathematical - indeed, the paper _cites_ the relevant formalism near the end of Section 2. However, this work does not present any such model. Without one, it is unreasonable to make the sort of security claims that the paper makes, as all such claims are relative to _some_ security model. For example, deniability means more than simply extracting a plausible message distinct to the intended message: it should be difficult for an adversary to tell whether the message they received came from the "real" key or an alternative key and whether the message came from the "real" message generation process or a fake one. I didn't see any claims of this sort at all in the latter part of the paper, only claims about the experimental results. Without some kind of theoretical claim on the security of the system ("security" here meaning "according to a goal and set of threats specified by the security model"), it doesn't seem possible to claim that the system provides deniability or improves security (or even doesn't harm it!) in any specific use case.

The rejoinder to this could be that the paper implicitly adopts the formalism of Canetti et al. ,'97. But in fact the approach taken is very different: in this work, the encryption algorithm itself provides the "fake" random choices through the supply of a decoy key. Is this detectable by an adversary? It is not shown here that it is not.

A much more minor point, but an important and closely related one: much is made in the argument against detection of the fact that the encoder's compression capability is good, in the sense that an encoded data stream should be indistinguishable from random in a frequency and correlation sense. In fact, it is a simple enough theorem in cryptography to be assigned as a problem on an undergraduate problem set that there exists a function which passes _any_ battery of tests for randomness and yet does not meet the formal requirements of a pseudorandom generator, in the sense that an adversary can perfectly predict its outputs given enough observations of its behavior. Statistical tests have a one-sided error here, but are being relied on for the wrong "direction" of the security argument (i.e., _failing_ the statistical tests would cause us to _reject_ the security of this scheme, but _passing_ them is not an argument _for_ such security). Indeed, the claim being "tested" here, that the encoded data stream be "indistinguishable from white noise" is a claim that the encoder itself is a semantically secure encryption scheme! (It very clearly is not - knowledge of the model used conveys a lot of information that could be used to distinguish the encodings of different "true" messages).

Lastly and an extremely minor point: Canetti's first name is "Ran", not "Rein" as the reference has it.

### Questions
Can the paper provide a clear security model? By this, I don't mean there has to be a mathematical definition of deniability and a proof the scheme meets it (although that would be nice). But it would be good at a minimum to say what an adversary's goals, capabilities, and limitations are in enough detail that claims about the detection of alternative messages can be evaluated for security other than by way of examples.

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed plausible deniability encryption, which can provide a plausible message instead of actual plaintext when a wrong secret key is used for decryption. In reality, the standard block cipher AES is used as the encryption scheme, and the expected answer is generated using LM with the prompt to guide the desired plausible message.

### Strengths
It is interesting that they propose a new cryptographic primitive by mixing the standard encryption method and language models.

### Weaknesses
However, by using the encryption algorithm as a simple module, many hints may actually be provided to the attacker at the interface between them. 

This assumes that LM also operates like an encryption scheme. In fact, the core to creating deniable encryption lies in LM, so AES operates only as an output encryptor in the proposed scheme. Thus, it appears to rely only on LM when analyzing the security or characteristics of actual deniable encryption. Excluding AES, the evidence for whether the proposed LM is a reliable encryption method appears to be weak other than the assumption that it "looks random."

### Questions
Does the proposed method assume a scenario that can be applied in practice? It seems that an attacker would also be able to see that EOS was broken, and thus he/she realizes that the wrong key was used and the output message is not real.
What is the reason for saying encoded plaintext is indistinguishable? Can the encoding be considered an encryption scheme? So why do you need AES?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Plausibly deniable encryption allows to open encrypted messages with multiple keys, providing valid decryptions for each key. This is used as a measure to protect against adversarial parties even when they are able to steal a key, as obtaining a coherent decrypted message does ensure it is the correct one.

Current schemes of plausible deniable encryption are either prohibitively expensive or only allow the decryption of a fixed set of keys. In the latter, the proposed defense is limited as it only increases the space of solutions by a constant factor. 

The current work overcomes the limitations of previous approaches by providing a technique that allows to open plausible messages for each possible key of the encryption scheme in an efficient manner. This is achieved by combining encryption, compression techniques used in large language models and Huffman codes. The work evaluates which parameters impact in the probability of detection of correct messages. Under certain conditions, the proposed scheme shows resilience to frequency, correlation and information theoretical tests that attempt to differentiate between true and decoy messages.

### Strengths
The paper presents a strong contribution: 

- The proposed scheme is original, leveraging the potential of LLMs and information theory in a creative manner. The link between information compression and security has a large potential.

- The authors did a very good job explaining key concepts of their contribution. 

- The paper presents an extensive evaluation, providing a clear picture of the situations in which the proposed scheme is applicable and the situations in which is not. Results show that encoded messages are undetected by statistical tests in many realistic scenarios. 

- The impact of the contribution is well motivated. The security of encrypted information exchanges benefit from a substantial enhancement if eavesdroppers are not sure that they have decrypted the correct message even having the key.

### Weaknesses
A fairly minor weakness that I see is the definition of security of the scheme. The properties outlined in Section 4 to avoid detection seem to make sense, but I think that property (1) could be more precise. For example in regular encryption, ciphertexts must be computationally random, i.e., no polynomial time adversary must be able to distinguish between real noise and the ciphertext. I think such a strong concept of random numbers are not needed for the encoding level of the scheme. However, I get the impression that frequency and correlation tests fit well to evaluate general purpose PRGs, but may fail into assess the lack of a stronger level of randomness.

### Questions
As mentioned above, I think the clarity on the detection aspect pointed above is fairly minor but I would be interested to know if the authors have additional insights on how strongly random the encodings should look.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
