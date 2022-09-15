'use strict';

import { GetCommand } from "@aws-sdk/lib-dynamodb";
import { PutCommand } from "@aws-sdk/lib-dynamodb";
import { DynamoDBClient } from "@aws-sdk/client-dynamodb";
import { DynamoDBDocumentClient } from "@aws-sdk/lib-dynamodb";

const REGION = "us-east-2";
const ddbClient = new DynamoDBClient({ region: REGION });

const marshallOptions = {
    // Whether to automatically convert empty strings, blobs, and sets to `null`.
    convertEmptyValues: false, // false, by default.
    // Whether to remove undefined values while marshalling.
    removeUndefinedValues: false, // false, by default.
    // Whether to convert typeof object to map attribute.
    convertClassInstanceToMap: false, // false, by default.
};
const unmarshallOptions = {
    // Whether to return numbers as a string instead of converting them to native JavaScript numbers.
    wrapNumbers: false, // false, by default.
};
const translateConfig = { marshallOptions, unmarshallOptions };
const ddbDocClient = DynamoDBDocumentClient.from(ddbClient, translateConfig);

import { createRequire } from 'module';
const require = createRequire(import.meta.url);
const plot_json = require("./plot.json");
console.log(plot_json);

const put_params = {
    TableName: "plotsV2",
    Item: {
        "key": "jira",
        "value": plot_json,
    },
};
const put = async () => {
    try {
        const data = await ddbDocClient.send(new PutCommand(put_params));
        console.log("Success - item added or updated", data);
        return data;
    } catch (err) {
        console.log("Error", err);
    }
};
// put();

const get_params = {
    TableName: "plotsV2",

    Key: {
        "key": "jira",
    },
};
const get = async () => {
    try {
        const data = await ddbDocClient.send(new GetCommand(get_params));
        console.log("Success :", data);
        console.log("Success :", data.Item.value);
        return data;
    } catch (err) {
        console.log("Error", err);
    }
};
get();
