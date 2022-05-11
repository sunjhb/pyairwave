# Airwave API 开发文档

## 通过API认证

AirWave 要求所有 API 请求通过 /LOGIN 进行身份验证，通过认证以后获取一个名为 X-BISCOTTI token 和 cookie。 AirWave API 请求必须在Headers中包含此 cookie 和 token
才能完成身份验证并获取到资源，并且可以防止跨站点请求伪造 (CSRF) 攻击。

> 请求URI：

```http request
https://{{host}}/LOGIN
```

> 请求Headers

```json
{
  "Content-Type": "application/x-www-form-urlencoded"
}
```

> 请求Body

```json
{
  "credential_0": "amp username",
  "credential_1": "amp password",
  "destination": "/api"
}
```

> 请求结果

请求结果获得cookie 和 headers中的X-BISCOTTI作为token


## 通过API获取终端Detail

获取终端detail的api仅支持单个终端查询，因此在请求中除了携带cookie和token以外，还需携带终端mac地址作为请求参数。这里以mac地址 00:0E:35:52:8C:AB举例
> 请求URI：

```http request
https://{{host}}/client_detail.xml?mac={{client-mac}}}
```

> 单终端请求URI：

```http request
https://{{host}}/client_detail.xml?mac=00:0E:35:52:8C:AB
```

> 多个终端请求URI：

```http request
https://{{host}}/client_detail.xml?mac=00:0E:35:52:8C:AB&mac=11:22:33:44:55:66
```

**注意mac地址中的字母必须是大写**

> 请求Headers

```json
{
  "Content-Type": "application/xml",
  "X-BISCOTTI": "通过认证获得的token",
  "Cookie": "通过认证获得的cookie"
}
```

> 请求结果example

```xml
<?xml version="1.0" encoding="ISO-8859-1" standalone="yes"?>

<amp:amp_client_detail version="1" xmlns:amp="http://www.airwave.com" 

     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 

     xsi:schemaLocation="http://www.airwave.com amp_client_detail.xsd">

  <client mac="00:0E:35:52:8C:AB">

    <ap id="3645">LWAPP-1250-1</ap>

    <assoc_stat>true</assoc_stat>

    <association id="1962">

      <ap id="79">ORiNOCO-AP-700-55-e6-e1</ap>

      <bytes_used>135357</bytes_used>

      <connect_time>2006-10-04T11:22:43-07:00</connect_time>

      <disconnect_time>2006-10-04T11:27:30-07:00</disconnect_time>

      <lan_elements>

        <lan hostname="bob.acmeville.org" ip_address="192.1.50.102" />

        <lan hostname="cats.awesome.com" ip_address="26:1F89:1820:A:98:7A:75AD:53B" />

      </lan_elements>

      <rssi>36</rssi>

    </association>

    <association id="1961">

      <ap id="79">ORiNOCO-AP-700-55-e6-e1</ap>

      <bytes_used>512</bytes_used>

      <connect_time>2006-10-04T11:19:12-07:00</connect_time>

      <disconnect_time>2006-10-04T11:20:13-07:00</disconnect_time>

      <vpn_elements>

        <vpn hostname="bob.acmeville.org" ip_address="192.1.1.1" />

      </vpn_elements>

      <rssi>38</rssi>

    </association>

    <auth_stat>false</auth_stat>

    <connect_time>2006-10-04T11:48:19-07:00</connect_time>

    <lan_elements>

      <lan hostname="cats.awesome.com" ip_address="26:1F89:1820:A:98:7A:75AD:53B" />

    </lan_elements>

    <rssi>0</rssi>

    <signal>-42</signal>

    <snr>0</snr>

    <vendor>Intel</vendor>

  </client>

</amp:amp_client_detail>
```

