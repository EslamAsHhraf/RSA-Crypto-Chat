# <img  align="center" width= 60px  src="https://media0.giphy.com/media/ocVFpiaTCxly9SKDit/giphy.gif?cid=ecf05e474dcd6b16fb6zacuya6rd00a9l4fzqvls9039kdvc&ep=v1_stickers_search&rid=giphy.gif&ct=s">RSA

<div align="center">

<img height=400px src="https://cdn.dribbble.com/users/7813810/screenshots/17447483/media/2f93ce55516c9b590bec1c8950a67a62.gif">
<div align="center">

### "Protect yourself from hacker attacking. 👨‍💻"

</div>
</div>

<hr style="background-color: #4b4c60"></hr>

## <img align= center width=50px height=50px src="https://user-images.githubusercontent.com/71986226/154075883-2a5679d2-b411-448f-b423-9565babf35aa.gif"> Table of Contents

- <a href ="#about"> 📙 Overview</a>
- <a href ="#started"> 🚀 Get Started</a>
- <a href ="#analysis"> 📉 Encryption/Decryption Analysis</a>
- <a href ="#Contributors"> ✨ Contributors</a>
- <a href ="#License"> 🔒 License</a>
<hr style="background-color: #4b4c60"></hr>
<a id = "about"></a>

## <img align="center"   width =60px  height =70px src="https://media2.giphy.com/media/Yn4nioYWSZMqiPNVuD/giphy.gif?cid=ecf05e47m5h78yoqhdkg8pq54o5qsxhdoltjxyfe08d4vxvg&rid=giphy.gif&ct=s"> Overview

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
<li><a href="https://github.com/EslamAsHhraf/RSA/blob/main/Report.pdf">Report</a></li>
<li>Built using <a href="https://docs.python.org/3/">Python</a></li>
</ul>
<hr style="background-color: #4b4c60"></hr>
<a id = "started"></a>

## <img  align= center width=50px height=50px src="https://c.tenor.com/HgX89Yku5V4AAAAi/to-the-moon.gif"> Get Started

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

## <img  align="center" width= 70px height =55px src="https://media1.giphy.com/media/DDGQgJLkOlSKe08e74/giphy.gif?cid=ecf05e477vz4x0fwe8vfh8ka9hbrdol4nev48hohq1ee3lfv&ep=v1_stickers_search&rid=giphy.gif&ct=s"> Encryption/Decryption Analysis

<table>

<tr>
<th width="60%">Graph</th>
<th>Analysis</th>
</tr>
<tr>
<td><img src="https://github.com/EslamAsHhraf/RSA/assets/71986226/34fb9a3c-7680-4adc-a84b-9345b798d161"></td>
<td>
Key size doesn’t affect Time of encryption and decryption [time almost zero] because algorithm has simple operations like addition and power …etc
</td>
</tr>
<tr>
<td><img src="https://github.com/EslamAsHhraf/RSA/assets/71986226/81d770d4-6246-49b5-9e0c-f43b01760c35"></td>
<td>
Time increases exponentially by increasing number of bits
</td>
</tr>
</table>

<hr style="background-color: #4b4c60"></hr>
<a id ="Contributors"></a>

## <img  align="center" width= 70px height =55px src="https://media0.giphy.com/media/Xy702eMOiGGPzk4Zkd/giphy.gif?cid=ecf05e475vmf48k83bvzye3w2m2xl03iyem3tkuw2krpkb7k&rid=giphy.gif&ct=s"> Contributors

<br>
<table >
  <tr>
        <td align="center"><a href="https://github.com/EslamAsHhraf"><img src="https://avatars.githubusercontent.com/u/71986226?v=4" width="150px;" alt=""/><br /><sub><b>Eslam Ashraf</b></sub></a><br /></td>
  </tr>
</table>

<hr style="background-color: #4b4c60"></hr>

<a id ="License"></a>

## 🔒 License

> **Note**: This software is licensed under MIT License, See [License](https://github.com/EslamAsHhraf/RSA/blob/main/LICENSE) for more information ©EslamAsHhraf.
