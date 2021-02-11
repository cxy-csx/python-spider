/***************************
*author: 逍遥子
*weixin: 哥们并肩走过
*software: node.js 
*time: 2021-02-10 22:21 
*description： 微信公众号密码加密算法
****************************/

var t;
var n;
var i;
var e;

function d(e, t) {
    var n = (65535 & e) + (65535 & t);
    return (e >> 16) + (t >> 16) + (n >> 16) << 16 | 65535 & n
}
function s(e, t, n, i, o, r) {
    return d((a = d(d(t, e), d(i, r))) << (s = o) | a >>> 32 - s, n);
    var a, s
}
function p(e, t, n, i, o, r, a) {
    return s(t & n | ~t & i, e, t, o, r, a)
}
function f(e, t, n, i, o, r, a) {
    return s(t & i | n & ~i, e, t, o, r, a)
}
function h(e, t, n, i, o, r, a) {
    return s(t ^ n ^ i, e, t, o, r, a)
}
function m(e, t, n, i, o, r, a) {
    return s(n ^ (t | ~i), e, t, o, r, a)
}
function l(e, t) {
    e[t >> 5] |= 128 << t % 32,
    e[14 + (t + 64 >>> 9 << 4)] = t;
    var n, i, o, r, a, s = 1732584193, l = -271733879, u = -1732584194, c = 271733878;
    for (n = 0; n < e.length; n += 16)
        s = p(i = s, o = l, r = u, a = c, e[n], 7, -680876936),
        c = p(c, s, l, u, e[n + 1], 12, -389564586),
        u = p(u, c, s, l, e[n + 2], 17, 606105819),
        l = p(l, u, c, s, e[n + 3], 22, -1044525330),
        s = p(s, l, u, c, e[n + 4], 7, -176418897),
        c = p(c, s, l, u, e[n + 5], 12, 1200080426),
        u = p(u, c, s, l, e[n + 6], 17, -1473231341),
        l = p(l, u, c, s, e[n + 7], 22, -45705983),
        s = p(s, l, u, c, e[n + 8], 7, 1770035416),
        c = p(c, s, l, u, e[n + 9], 12, -1958414417),
        u = p(u, c, s, l, e[n + 10], 17, -42063),
        l = p(l, u, c, s, e[n + 11], 22, -1990404162),
        s = p(s, l, u, c, e[n + 12], 7, 1804603682),
        c = p(c, s, l, u, e[n + 13], 12, -40341101),
        u = p(u, c, s, l, e[n + 14], 17, -1502002290),
        s = f(s, l = p(l, u, c, s, e[n + 15], 22, 1236535329), u, c, e[n + 1], 5, -165796510),
        c = f(c, s, l, u, e[n + 6], 9, -1069501632),
        u = f(u, c, s, l, e[n + 11], 14, 643717713),
        l = f(l, u, c, s, e[n], 20, -373897302),
        s = f(s, l, u, c, e[n + 5], 5, -701558691),
        c = f(c, s, l, u, e[n + 10], 9, 38016083),
        u = f(u, c, s, l, e[n + 15], 14, -660478335),
        l = f(l, u, c, s, e[n + 4], 20, -405537848),
        s = f(s, l, u, c, e[n + 9], 5, 568446438),
        c = f(c, s, l, u, e[n + 14], 9, -1019803690),
        u = f(u, c, s, l, e[n + 3], 14, -187363961),
        l = f(l, u, c, s, e[n + 8], 20, 1163531501),
        s = f(s, l, u, c, e[n + 13], 5, -1444681467),
        c = f(c, s, l, u, e[n + 2], 9, -51403784),
        u = f(u, c, s, l, e[n + 7], 14, 1735328473),
        s = h(s, l = f(l, u, c, s, e[n + 12], 20, -1926607734), u, c, e[n + 5], 4, -378558),
        c = h(c, s, l, u, e[n + 8], 11, -2022574463),
        u = h(u, c, s, l, e[n + 11], 16, 1839030562),
        l = h(l, u, c, s, e[n + 14], 23, -35309556),
        s = h(s, l, u, c, e[n + 1], 4, -1530992060),
        c = h(c, s, l, u, e[n + 4], 11, 1272893353),
        u = h(u, c, s, l, e[n + 7], 16, -155497632),
        l = h(l, u, c, s, e[n + 10], 23, -1094730640),
        s = h(s, l, u, c, e[n + 13], 4, 681279174),
        c = h(c, s, l, u, e[n], 11, -358537222),
        u = h(u, c, s, l, e[n + 3], 16, -722521979),
        l = h(l, u, c, s, e[n + 6], 23, 76029189),
        s = h(s, l, u, c, e[n + 9], 4, -640364487),
        c = h(c, s, l, u, e[n + 12], 11, -421815835),
        u = h(u, c, s, l, e[n + 15], 16, 530742520),
        s = m(s, l = h(l, u, c, s, e[n + 2], 23, -995338651), u, c, e[n], 6, -198630844),
        c = m(c, s, l, u, e[n + 7], 10, 1126891415),
        u = m(u, c, s, l, e[n + 14], 15, -1416354905),
        l = m(l, u, c, s, e[n + 5], 21, -57434055),
        s = m(s, l, u, c, e[n + 12], 6, 1700485571),
        c = m(c, s, l, u, e[n + 3], 10, -1894986606),
        u = m(u, c, s, l, e[n + 10], 15, -1051523),
        l = m(l, u, c, s, e[n + 1], 21, -2054922799),
        s = m(s, l, u, c, e[n + 8], 6, 1873313359),
        c = m(c, s, l, u, e[n + 15], 10, -30611744),
        u = m(u, c, s, l, e[n + 6], 15, -1560198380),
        l = m(l, u, c, s, e[n + 13], 21, 1309151649),
        s = m(s, l, u, c, e[n + 4], 6, -145523070),
        c = m(c, s, l, u, e[n + 11], 10, -1120210379),
        u = m(u, c, s, l, e[n + 2], 15, 718787259),
        l = m(l, u, c, s, e[n + 9], 21, -343485551),
        s = d(s, i),
        l = d(l, o),
        u = d(u, r),
        c = d(c, a);
    return [s, l, u, c]
}
function u(e) {
    var t, n = "";
    for (t = 0; t < 32 * e.length; t += 8)
        n += String.fromCharCode(e[t >> 5] >>> t % 32 & 255);
    return n
}
function c(e) {
    var t, n = [];
    for (n[(e.length >> 2) - 1] = void 0,
    t = 0; t < n.length; t += 1)
        n[t] = 0;
    for (t = 0; t < 8 * e.length; t += 8)
        n[t >> 5] |= (255 & e.charCodeAt(t / 8)) << t % 32;
    return n
}
function i(e) {
    var t, n, i = "0123456789abcdef", o = "";
    for (n = 0; n < e.length; n += 1)
        t = e.charCodeAt(n),
        o += i.charAt(t >>> 4 & 15) + i.charAt(15 & t);
    return o
}
function o(e) {
    return unescape(encodeURIComponent(e))
}
function r(e) {
    return u(l(c(t = o(e)), 8 * t.length));
    var t
}
function a(e, t) {
    return function(e, t) {
        var n, i, o = c(e), r = [], a = [];
        for (r[15] = a[15] = void 0,
        16 < o.length && (o = l(o, 8 * e.length)),
        n = 0; n < 16; n += 1)
            r[n] = 909522486 ^ o[n],
            a[n] = 1549556828 ^ o[n];
        return i = l(r.concat(c(t)), 512 + 8 * t.length),
        u(l(a.concat(i), 640))
    }(o(e), o(t))
}
function getpwd(e, t, n) {
    return t ? n ? a(t, e) : i(a(t, e)) : n ? r(e) : i(r(e))
}

console.log(getpwd('123456'))  // e10adc3949ba59abbe56e057f20f883e