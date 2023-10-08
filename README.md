# 🔐 RSA

<div align="center">

<img height=400px src="https://cdn.dribbble.com/users/7813810/screenshots/17447483/media/2f93ce55516c9b590bec1c8950a67a62.gif">
<div align="center">

### "Protect yourself from hacker attacking. 👨‍💻"

</div>
</div>

<hr style="background-color: #4b4c60"></hr>

## 📝 Table of Contents

- <a href ="#about"> 📙 Overview</a>
- <a href ="#started"> 🚀 Get Started</a>
- <a href ="#analysis"> 📉 Encryption/Decryption Analysis</a>
- <a href ="#Contributors"> ✨ Contributors</a>
- <a href ="#License"> 🔒 License</a>
<hr style="background-color: #4b4c60"></hr>
<a id = "about"></a>

## 📙 Overview

<ul>
 <li>
The RSA algorithm (Rivest-Shamir-Adleman) is the basis of a cryptosystem -- a suite of cryptographic algorithms that are used for specific security services or purposes -- which enables public key encryption and is widely used to secure sensitive data, particularly when it is being sent over an insecure network such as the internet.</li> 
<li>How does the RSA algorithm work?</li>
<br>
<ul> <li>Alice generates her RSA keys by selecting two primes: p=11 and q=13. The modulus is n=p*q=143. The totient is n ϕ(n)=(p−1)x(q−1)=120. She chooses 7 for her RSA public key e and calculates her RSA private key using the Extended Euclidean algorithm, which gives her 103</li>
<li>Bob wants to send Alice an encrypted message, M, so he obtains her RSA public key (n, e) which, in this example, is (143, 7). His plaintext message is just the number 9 and is encrypted into ciphertext, C, as follows</li>
<ul>
<li>M^e mod n = 9^7mod 143 = 48 = C</li>
</ul>
<li>When Alice receives Bob's message, she decrypts it by using her RSA private key (d, n) as follows:</li>
<ul>
<li>C^d mod n = 48^103 mod 143 = 9 = M</li>
</ul>
</ul>
<li><a href="https://github.com/EslamAsHhraf/RSA-Crypto-Chat/blob/main/Requirement.pdf">Requirements</a></li>
<li>Built using <a href="https://docs.python.org/3/">Python</a></li>
</ul>
<hr style="background-color: #4b4c60"></hr>
<a id = "started"></a>

## 🚀 Get Started

- Navigate to the src directory

```sh
cd src
```

- To start chatting
    - Run the `server.py` file
    - Run the `client.py` file

- Run the `attack.py` file to get how size of input affect Time of encryption and decryption
- Run the `speed_encryption_decryption.py` file to get how size of input affect Time of encryption and decryption


<br>

<hr style="background-color: #4b4c60"></hr>
<a id ="analysis"></a>

## 📉  Encryption/Decryption Analysis

<table>

<tr>
<th width="60%">Graph</th>
<th>Analysis</th>
</tr>
<tr>
<td><img src="https://github.com/EslamAsHhraf/RSA-Crypto-Chat/assets/71986226/926d6716-c454-492b-ad53-d485da3f67fa"></td>
<td>
Key size doesn’t affect Time of encryption and decryption [time almost zero] because algorithm has simple operations like addition and power …etc
</td>
</tr>
<tr>
<td><img src="https://github.com/EslamAsHhraf/RSA-Crypto-Chat/assets/71986226/10549276-bc27-4cd4-a21a-c44b414edb40"></td>
<td>
Time increases exponentially by increasing number of bits
</td>
</tr>
</table>

<hr style="background-color: #4b4c60"></hr>
<a id ="Contributors"></a>

## 👑 Contributors

<br>
<table >
  <tr>
        <td align="center"><a href="https://github.com/EslamAsHhraf"><img src="https://avatars.githubusercontent.com/u/71986226?v=4" width="150px;" alt=""/><br /><sub><b>Eslam Ashraf</b></sub></a><br /></td>
  </tr>
</table>

<hr style="background-color: #4b4c60"></hr>

<a id ="License"></a>

## 🔒 License

> **Note**: This software is licensed under MIT License, See [License](https://github.com/EslamAsHhraf/RSA-Crypto-Chat/blob/main/LICENSE) for more information ©EslamAsHhraf.
