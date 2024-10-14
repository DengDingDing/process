# -*- coding: utf-8 -*-

from xml.dom import minidom
import os
import glob

lut = {}
lut["i1"] = 0
lut["i10"] = 1
lut["i11"] = 2
lut["i12"] = 3
lut["i13"] = 4
lut["i14"] = 5
lut["i15"] = 6
lut["i2"] = 7
lut["i3"] = 8
lut["i4"] = 9
lut["i5"] = 10
lut["il100"] = 11
lut["il110"] = 12
lut["il50"] = 13
lut["il60"] = 14
lut["il70"] = 15
lut["il80"] = 16
lut["il90"] = 17
lut["io"] = 18
lut["ip"] = 19
lut["p1"] = 20
lut["p10"] = 21
lut["p11"] = 22
lut["p12"] = 23
lut["p13"] = 24
lut["p14"] = 25
lut["p15"] = 26
lut["p16"] = 27
lut["p17"] = 28
lut["p18"] = 29
lut["p19"] = 30
lut["p2"] = 31
lut["p20"] = 32
lut["p21"] = 33
lut["p22"] = 34
lut["p23"] = 35
lut["p24"] = 36
lut["p25"] = 37
lut["p26"] = 38
lut["p27"] = 39
lut["p28"] = 40
lut["p3"] = 41
lut["p4"] = 42
lut["p5"] = 43
lut["p6"] = 44
lut["p7"] = 45
lut["p8"] = 46
lut["p9"] = 47
lut["pa10"] = 48
lut["pa12"] = 49
lut["pa13"] = 50
lut["pa14"] = 51
lut["pa8"] = 52
lut["pb"] = 53
lut["pc"] = 54
lut["pg"] = 55
lut["ph1.5"] = 56
lut["ph2"] = 57
lut["ph2.1"] = 58
lut["ph2.2"] = 59
lut["ph2.4"] = 60
lut["ph2.5"] = 61
lut["ph2.8"] = 62
lut["ph2.9"] = 63
lut["ph3"] = 64
lut["ph3.2"] = 65
lut["ph3.5"] = 66
lut["ph3.8"] = 67
lut["ph4"] = 68
lut["ph4.2"] = 69
lut["ph4.3"] = 70
lut["ph4.5"] = 71
lut["ph4.8"] = 72
lut["ph5"] = 73
lut["ph5.3"] = 74
lut["ph5.5"] = 75
lut["pl10"] = 76
lut["pl100"] = 77
lut["pl110"] = 78
lut["pl120"] = 79
lut["pl15"] = 80
lut["pl20"] = 81
lut["pl25"] = 82
lut["pl30"] = 83
lut["pl35"] = 84
lut["pl40"] = 85
lut["pl5"] = 86
lut["pl50"] = 87
lut["pl60"] = 88
lut["pl65"] = 89
lut["pl70"] = 90
lut["pl80"] = 91
lut["pl90"] = 92
lut["pm10"] = 93
lut["pm13"] = 94
lut["pm15"] = 95
lut["pm1.5"] = 96
lut["pm2"] = 97
lut["pm20"] = 98
lut["pm25"] = 99
lut["pm30"] = 100
lut["pm35"] = 101
lut["pm40"] = 102
lut["pm46"] = 103
lut["pm5"] = 104
lut["pm50"] = 105
lut["pm55"] = 106
lut["pm8"] = 107
lut["pn"] = 108
lut["pne"] = 109
lut["po"] = 110
lut["pr10"] = 111
lut["pr100"] = 112
lut["pr20"] = 113
lut["pr30"] = 114
lut["pr40"] = 115
lut["pr45"] = 116
lut["pr50"] = 117
lut["pr60"] = 118
lut["pr70"] = 119
lut["pr80"] = 120
lut["ps"] = 121
lut["pw2"] = 122
lut["pw2.5"] = 123
lut["pw3"] = 124
lut["pw3.2"] = 125
lut["pw3.5"] = 126
lut["pw4"] = 127
lut["pw4.2"] = 128
lut["pw4.5"] = 129
lut["w1"] = 130
lut["w10"] = 131
lut["w12"] = 132
lut["w13"] = 133
lut["w16"] = 134
lut["w18"] = 135
lut["w20"] = 136
lut["w21"] = 137
lut["w22"] = 138
lut["w24"] = 139
lut["w28"] = 140
lut["w3"] = 141
lut["w30"] = 142
lut["w31"] = 143
lut["w32"] = 144
lut["w34"] = 145
lut["w35"] = 146
lut["w37"] = 147
lut["w38"] = 148
lut["w41"] = 149
lut["w42"] = 150
lut["w43"] = 151
lut["w44"] = 152
lut["w45"] = 153
lut["w46"] = 154
lut["w47"] = 155
lut["w48"] = 156
lut["w49"] = 157
lut["w5"] = 158
lut["w50"] = 159
lut["w55"] = 160
lut["w56"] = 161
lut["w57"] = 162
lut["w58"] = 163
lut["w59"] = 164
lut["w60"] = 165
lut["w62"] = 166
lut["w63"] = 167
lut["w66"] = 168
lut["w8"] = 169
lut["wo"] = 170
lut["i6"] = 171
lut["i7"] = 172
lut["i8"] = 173
lut["i9"] = 174
lut["ilx"] = 175
lut["p29"] = 176
lut["w29"] = 177
lut["w33"] = 178
lut["w36"] = 179
lut["w39"] = 180
lut["w4"] = 181
lut["w40"] = 182
lut["w51"] = 183
lut["w52"] = 184
lut["w53"] = 185
lut["w54"] = 186
lut["w6"] = 187
lut["w61"] = 188
lut["w64"] = 189
lut["w65"] = 190
lut["w67"] = 191
lut["w7"] = 192
lut["w9"] = 193
lut["pax"] = 194
lut["pd"] = 195
lut["pe"] = 196
lut["phx"] = 197
lut["plx"] = 198
lut["pmx"] = 199
lut["pnl"] = 200
lut["prx"] = 201
lut["pwx"] = 202
lut["w11"] = 203
lut["w14"] = 204
lut["w15"] = 205
lut["w17"] = 206
lut["w19"] = 207
lut["w2"] = 208
lut["w23"] = 209
lut["w25"] = 210
lut["w26"] = 211
lut["w27"] = 212
lut["pl0"] = 213
lut["pl4"] = 214
lut["pl3"] = 215
lut["pm2.5"] = 216
lut["ph4.4"] = 217
lut["pn40"] = 218
lut["ph3.3"] = 219
lut["ph2.6"] = 220


def convert_coordinates(size, box):
    dw = 1.0/size[0]
    dh = 1.0/size[1]
    x = (box[0]+box[1])/2.0
    y = (box[2]+box[3])/2.0
    w = box[1]-box[0]
    h = box[3]-box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_xml2yolo( lut ):

    for fname in glob.glob("*.xml"):
        
        xmldoc = minidom.parse(fname)
        
        fname_out = (fname[:-4]+'.txt')

        with open(fname_out, "w") as f:

            itemlist = xmldoc.getElementsByTagName('object')
            size = xmldoc.getElementsByTagName('size')[0]
            width = int((size.getElementsByTagName('width')[0]).firstChild.data)
            height = int((size.getElementsByTagName('height')[0]).firstChild.data)

            for item in itemlist:
                # get class label
                classid =  (item.getElementsByTagName('name')[0]).firstChild.data
                if classid in lut:
                    label_str = str(lut[classid])
                else:
                    label_str = "-1"
                    print ("warning: label '%s' not in look-up table" % classid)

                # get bbox coordinates
                xmin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmin')[0]).firstChild.data
                ymin = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymin')[0]).firstChild.data
                xmax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('xmax')[0]).firstChild.data
                ymax = ((item.getElementsByTagName('bndbox')[0]).getElementsByTagName('ymax')[0]).firstChild.data
                b = (float(xmin), float(xmax), float(ymin), float(ymax))
                bb = convert_coordinates((width,height), b)
                #print(bb)

                f.write(label_str + " " + " ".join([("%.6f" % a) for a in bb]) + '\n')

        print ("wrote %s" % fname_out)



def main():
    convert_xml2yolo( lut )


if __name__ == '__main__':
    main()